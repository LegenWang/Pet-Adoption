"""Tests for the pets API"""

import unittest
from flask import Flask
from main import pets_blueprint

class PetBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the Flask application for testing"""
        self.app = Flask(__name__)
        self.app.register_blueprint(pets_blueprint)
        self.client = self.app.test_client()
        self.app.testing = True

    def test_get_pets(self):
        """Test the GET / endpoint"""
        response = self.client.get('/pets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertIn('Buddy', str(response.data))

    def test_get_pet_found(self):
        """Test retrieving a pet by ID that exists"""
        response = self.client.get('/pets/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Buddy')

    def test_get_pet_not_found(self):
        """Test retrieving a pet by ID that does not exist"""
        response = self.client.get('/pets/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Pet not found', str(response.data))

if __name__ == '__main__':
    unittest.main()
