'''
test
'''
import pytest
from flask import Flask
from management import application_blueprint

# Configure the app for testing
@pytest.fixture
def test_client():
    """Fixture to configure the test client."""
    app = Flask(__name__)
    app.register_blueprint(application_blueprint)
    app.config['TESTING'] = True
    with app.test_client() as test_client_instance:
        yield test_client_instance

def test_get_applications(test_client):
    """Test retrieving all applications."""
    response = test_client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_application_success(test_client):
    """Test retrieving a specific application by ID."""
    response = test_client.get('/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_name'] == "Alice"

def test_get_application_not_found(test_client):
    """Test retrieving an application with an ID that does not exist."""
    response = test_client.get('/999')
    assert response.status_code == 404
    assert b'Application not found' in response.data

def test_manager_login_success(test_client):
    """Test successful manager login."""
    response = test_client.post('/manage_login', json={
        "manager_email": "admin@example.com",
        "manager_password": "password123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Login successful"

def test_manager_login_failure(test_client):
    """Test manager login with incorrect credentials."""
    response = test_client.post('/manage_login', json={
        "manager_email": "admin@example.com",
        "manager_password": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.get_json()
    assert data["message"] == "Invalid credentials"
