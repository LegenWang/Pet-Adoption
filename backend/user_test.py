''' Test file '''
import pytest
from users import user_blueprint
from flask import Flask
from data_base import initialize_database

class TestAPI:
    '''Class for all unit tests.'''
    client = None

    @pytest.fixture(autouse=True, scope='function')
    def setup_client(self):
        """Set up the test client for all tests."""

        # Initialize the database before running tests
        initialize_database()

        app = Flask(__name__)
        app.register_blueprint(user_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestAPI.client = test_client
            yield

    def test_login_success(self):
        """Test successful user login."""
        payload = {
            "username": "steven",
            "password": "1234567"
        }
        response = self.client.post('/login', json=payload)

        assert response.status_code == 200
        assert response.get_json()["username"] == "steven"

    def test_login_failure(self):
        """Test user login with incorrect credentials."""
        payload = {
            "username": "steven",
            "password": "wrongpassword"
        }
        response = self.client.post('/login', json=payload)

        assert response.status_code == 401
        assert response.get_json()["error"] == "Invalid username or password"

    def test_register_success(self):
        """Test successful user registration."""
        payload = {
            "username": "jason",
            "password": "newpassword"
        }
        response = self.client.post('/register', json=payload)

        assert response.status_code == 201
        assert response.get_json()["message"] == "User registered successfully"

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
        assert response.get_json()["error"] == "Username already exists"

# the main api is commented out for now so the test will be tested later
    # def test_logout_success(self):
    #     """Test successful user logout."""
    #     payload = {
    #         "username": "steven"
    #     }
    #     response = self.client.post('/logout', json=payload)

    #     assert response.status_code == 200
    #     assert response.get_json()["message"] == "User logged out successfully"

    # def test_logout_failure(self):
    #     """Test logout for a user who is not logged in."""
    #     payload = {
    #         "username": "rgebrgtrtg"
    #     }
    #     response = self.client.post('/logout', json=payload)

    #     assert response.status_code == 404
    #     assert response.get_json()["error"] == "User is not logged in"
