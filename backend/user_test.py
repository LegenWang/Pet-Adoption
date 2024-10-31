''' Test file '''
import pytest
from flask import Flask
from users import user_blueprint

@pytest.fixture
def client():
    """ Configure the test client."""
    app = Flask(__name__)
    app.register_blueprint(user_blueprint)
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_login_success(test_client):
    """Test successful user login."""
    response = test_client.post('/login', json={
        "username": "steven",
        "password": "1234567"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == "steven"

def test_login_failure(test_client):
    """Test user login with incorrect credentials."""
    response = test_client.post('/login', json={
        "username": "steven",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "Invalid username or password"

def test_register_success(test_client):
    """Test successful user registration."""
    response = test_client.post('/register', json={
        "username": "new_user",
        "password": "newpassword"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User registered successfully"

def test_register_username_exists(test_client):
    """Test user registration with an existing username."""
    test_client.post('/register', json={
        "username": "existing_user",
        "password": "password"
    })

    response = test_client.post('/register', json={
        "username": "existing_user",
        "password": "newpassword"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Username already exists"
