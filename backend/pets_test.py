"""Tests for the pets API"""
import pytest
from flask import Flask
from pets import pets_blueprint

class TestAPI:
    ''' class for all the unittests'''

    client = None

    @pytest.fixture(autouse=True, scope='function')
    def setup_client(self):
        """Setting up test client for all tests"""
        app = Flask(__name__)
        app.register_blueprint(pets_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestAPI.client = test_client
            yield

    def test_get_pets(self):
        """Test the GET / endpoint"""
        response = self.client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)  # Check that response is a list

    def test_get_pet_found(self):
        """Test retrieving a pet by ID that exists"""
        response = self.client.get('/1')
        assert response.status_code == 200
        data = response.get_json()
        assert data['name'] == 'Buddy'

    def test_get_pet_not_found(self):
        """Test retrieving a pet by ID that exists"""
        response = self.client.get('/999')
        assert response.status_code == 404
        data = response.get_json()
        assert data["error"] == "Pet not found"
