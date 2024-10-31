''' Test file '''
import pytest
from main import app 

@pytest.fixture
def client():
    '''Provides a test client for the Flask application used for making requests to the app '''
    app.testing = True
    with app.test_client() as test_client:
        yield test_client

def test_register_user(test_client):
    ''' Test the registration of a new user'''
    username = "janedoe"
    password = "randompassword123"
    
    response = test_client.post('/users/register', json={"username": username, "password": password})
    assert response.status_code == 201
    assert b"User registered successfully" in response.data

def test_register_existing_user(test_client):
    ''' Test registration attempt with an existing username'''
    username = "steven"
    password = "1234567"
    
    response = test_client.post('/users/register', json={"username": username, "password": password})
    assert response.status_code == 400
    assert b"Username already exists" in response.data

def test_login_user(test_client):
    ''' Test user login with correct credentials'''
    username = "james"
    password = "helloworld"
    
    response = test_client.post('/users/login', json={"username": username, "password": password})
    assert response.status_code == 200
    assert b"janedoe" in response.data  

def test_login_invalid_user(test_client):
    ''' Test login attempt with an invalid username'''
    invalid_username = "truman"
    invalid_password = "wrongpass"
    
    response = test_client.post('/users/login', json={"username": invalid_username, "password": invalid_password})
    assert response.status_code == 401
    assert b"Invalid username or password" in response.data

def test_login_invalid_password(test_client):
    ''' Test login attempt with an incorrect password'''
    username = "steven"
    invalid_password = "wrongpass"
    
    response = test_client.post('/users/login', json={"username": username, "password": invalid_password})
    assert response.status_code == 401
    assert b"Invalid username or password" in response.data
