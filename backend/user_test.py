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
    with app.test_client() as client:
        yield client

def test_login_success(client):
    """Test successful user login."""
    response = client.post('/login', json={
        "username": "steven",
        "password": "1234567"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == "steven"

def test_login_failure(client):
    """Test user login with incorrect credentials."""
    response = client.post('/login', json={
        "username": "steven",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "Invalid username or password"

def test_register_success(client):
    """Test successful user registration."""
    response = client.post('/register', json={
        "username": "new_user",
        "password": "newpassword"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User registered successfully"

def test_register_username_exists(client):
    """Test user registration with an existing username."""
    # First, register the user
    client.post('/register', json={
        "username": "existing_user",
        "password": "password"
    })

    # Attempt to register the same user again
    response = client.post('/register', json={
        "username": "existing_user",
        "password": "newpassword"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Username already exists"
