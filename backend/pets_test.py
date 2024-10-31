"""Tests for the pets API"""
import pytest
from pets import pets_blueprint

@pytest.fixture
def client():
    """Configure blueprint testing"""
    pets_blueprint.config['TESTING'] = True
    with pets_blueprint.test_client() as client:
        yield client

def test_get_pets(client):
    """Test the GET / endpoint"""
    response = client.get('/pets')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Check that response is a list

def test_get_pet_found(client):
    """Test retrieving a pet by ID that exists"""
    response = client.get('/pets/1')
    assert response.status_code == 200
    data = response.get_json()
    assert 'Buddy' in data

def test_get_pet_not_found(client):
    """Test retrieving a pet by ID that exists"""
    response = client.get('/pets/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Buddy'

    def test_get_pet_not_found(self):
        """Test retrieving a pet by ID that does not exist"""
        response = self.client.get('/pets/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Pet not found', str(response.data))
