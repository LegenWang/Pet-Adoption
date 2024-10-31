"""
Unit tests for the management module, including tests for application retrieval 
and manager login functionality.
"""
import pytest
from main import app

# Configure the app for testing
@pytest.fixture
def test_client():
    """Fixture to configure the test client."""
    app.testing = True
    with app.test_client() as test_client:
        yield test_client

def test_get_applications(test_client):
    """Test retrieving all applications."""
    response = test_client.get('/applications')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Check that response is a list
    assert len(data) > 0           # Check that there is at least one application

def test_get_application_success(test_client):
    """Test retrieving a specific application by ID."""
    response = test_client.get('/applications/1')  # Assuming ID 1 exists
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_name'] == "Alice"  # Check specific user data based on the mock data

def test_get_application_not_found(test_client):
    """Test retrieving an application with an ID that does not exist."""
    response = test_client.get('/applications/999')  # Assuming ID 999 does not exist
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
