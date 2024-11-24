''' Test file '''
import sqlite3
import pytest
from users import user_blueprint
from flask import Flask
from data_base import initialize_database, initialize_users_managers_database

class TestAPI:
    '''Class for all unit tests.'''
    client = None

    @pytest.fixture(autouse=True, scope='function')
    def setup_client(self):
        """Set up the test client for all tests."""

        # Initialize the database before running tests
        initialize_database()
        initialize_users_managers_database()

        # Clear any previous test data to avoid conflicts
        self.clear_test_data()

        app = Flask(__name__)
        app.register_blueprint(user_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestAPI.client = test_client
            yield

    def clear_test_data(self):
        """
        Clear all test data from the database.
        """
        connection = sqlite3.connect('users_managers.db')
        cursor = connection.cursor()

        # Remove any test users added during previous tests
        cursor.execute("DELETE FROM Users WHERE username IN ('jason')")

        connection.commit()
        connection.close()

    def test_login_success(self):
        """Test successful user login."""
        payload = {
            "username": "steven",
            "password": "1234567"
        }
        response = self.client.post('/login', json=payload)

        assert response.status_code == 200
        assert "Welcome back, steven!" in response.get_json()["message"]

    def test_login_failure(self):
        """Test user login with incorrect credentials."""
        payload = {
            "username": "steven",
            "password": "wrongpassword"
        }
        response = self.client.post('/login', json=payload)

        assert response.status_code == 401
        assert response.get_json()["error"] == "Invalid username/email or password"

    def test_register_success(self):
        """Test successful user registration."""
        payload = {
            "username": "jason",
            "email": "jason@example",
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
        assert response.get_json()["error"] == "Username or email already exists"

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
