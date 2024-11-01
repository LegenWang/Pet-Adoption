''' Test file '''
import pytest
from users import user_blueprint
from flask import Flask

class TestAPI:
    ''' class for all the unittests'''
    client = None

    @pytest.fixture(autouse=True, scope='function')

    def setup_client(self):
        """Setting up test client for all tests"""
        app = Flask(__name__)
        app.register_blueprint(user_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestAPI.client = test_client
            yield

    def test_login_success(self):
        """Test successful user login."""
        response = self.client.post('/login', json={
            "username": "steven",
            "password": "1234567"
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data["username"] == "steven"

    def test_login_failure(self):
        """Test user login with incorrect credentials."""
        response = self.client.post('/login', json={
            "username": "steven",
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        data = response.get_json()
        assert data["error"] == "Invalid username or password"

    def test_register_success(self):
        """Test successful user registration."""
        response = self.client.post('/register', json={
            "username": "jason",
            "password": "newpassword"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["message"] == "User registered successfully"

    def test_register_username_exists(self):
        """Test user registration with an existing username."""
        self.client.post('/register', json={
            "username": "james",
            "password": "helloworld"
        })

        response = self.client.post('/register', json={
            "username": "james",
            "password": "helloworld"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Username already exists"
