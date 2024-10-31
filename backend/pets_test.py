"""Tests for the pets API"""
import pytest
from flask import Flask
from pets import pets_blueprint

@pytest.fixture
def client():
    """ Configure the test client."""
    app = Flask(__name__)
    app.register_blueprint(pets_blueprint)
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

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
    response = client.get('/pets/999')
    assert response.status_code == 404

