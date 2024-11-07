"""test_management."""
import pytest
from flask import Flask
from management import application_blueprint
from data_base import initialize_database

class TestManagementAPI:
    """Class for all management API unit tests."""
    client = None

    @pytest.fixture(autouse=True, scope='function')
    def setup_client(self):
        """Setting up test client for all tests."""
        initialize_database()
        app = Flask(__name__)
        app.register_blueprint(application_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestManagementAPI.client = test_client
            yield

    def test_get_applications(self):
        """Test retrieving all applications."""
        response = self.client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

    def test_get_application_success(self):
        """Test retrieving a specific application by ID."""
        response = self.client.get('/1')  # Assuming ID 1 exists
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_name'] == "Alice"  # Check specific user data based on the mock data

    def test_get_application_not_found(self):
        """Test retrieving an application with an ID that does not exist."""
        response = self.client.get('/999')  # Assuming ID 999 does not exist
        assert response.status_code == 404
        assert b'Application not found' in response.data

    def test_manager_login_success(self):
        """Test successful manager login."""
        response = self.client.post('/manage_login', json={
            "manager_email": "admin@example.com",
            "manager_password": "password123"
        })
        assert response.status_code == 200
        data = response.get_json()
        assert "message" in data
        assert data["message"] == "Login successful"

    def test_manager_login_failure(self):
        """Test manager login with incorrect credentials."""
        response = self.client.post('/manage_login', json={
            "manager_email": "admin@example.com",
            "manager_password": "wrongpassword"
        })
        assert response.status_code == 401
        data = response.get_json()
        assert "message" in data
        assert data["message"] == "Invalid manager email or password"
