import pytest
from management import application_blueprint

# Configure the app for testing
@pytest.fixture
def client():
    """Fixture to configure the test client."""
    application_blueprint.config['TESTING'] = True
    with application_blueprint.test_client() as client:
        yield client

def test_get_applications(client):
    """Test retrieving all applications."""
    response = client.get('/applications')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Check that response is a list
    assert len(data) > 0           # Check that there is at least one application

def test_get_application_success(client):
    """Test retrieving a specific application by ID."""
    response = client.get('/applications/1')  # Assuming ID 1 exists
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_name'] == "Alice"  # Check specific user data based on the mock data

def test_get_application_not_found(client):
    """Test retrieving an application with an ID that does not exist."""
    response = client.get('/applications/999')  # Assuming ID 999 does not exist
    assert response.status_code == 404
    assert b'Application not found' in response.data

def test_manager_login_success(client):
    """Test successful manager login."""
    response = client.post('/manage_login', json={
        "manager_email": "admin@example.com",
        "manager_password": "password123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Login successful"

def test_manager_login_failure(client):
    """Test manager login with incorrect credentials."""
    response = client.post('/manage_login', json={
        "manager_email": "admin@example.com",
        "manager_password": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.get_json()
    assert data["message"] == "Invalid credentials"
