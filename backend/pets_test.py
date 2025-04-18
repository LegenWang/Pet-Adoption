"""Tests for the pets API"""
import pytest
from flask import Flask
from pets import pets_blueprint
from data_base import initialize_database

class TestAPI:
    ''' class for all the unittests'''

    client = None

    @pytest.fixture(autouse=True, scope='function')
    def setup_client(self):
        """Setting up test client for all tests"""
        initialize_database()
        app = Flask(__name__)
        app.register_blueprint(pets_blueprint)
        app.config['TESTING'] = True
        with app.test_client() as test_client:
            TestAPI.client = test_client
            yield

    def test_get_pets(self):
        """Test the GET / endpoint"""
        response_get = self.client.get('/')
        assert response_get.status_code == 200
        data = response_get.get_json()
        assert isinstance(data, list)
        assert len(data) > 0  # Ensure there are pets in the list
        assert data[0]["name"] == "Buddy"  # Check the first pet's name


    def test_get_pet_found(self):
        """Test retrieving a pet by ID that exists"""
        response_get = self.client.get('/1')
        assert response_get.status_code == 200
        data = response_get.get_json()
        assert data["name"] == "Buddy"
        assert data["breed"] == "Golden Retriever"

    def test_get_pet_not_found(self):
        """Test retrieving a pet by ID that doesn't exist"""
        response_get = self.client.get('/999')
        assert response_get.status_code == 404
        data = response_get.get_json()
        assert data["error"] == "Pet not found"
