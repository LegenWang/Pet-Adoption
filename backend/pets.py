from flask import Flask, request, jsonify, Blueprint
pets_blueprint = Blueprint('pets', __name__)

pets = [
    {"id": 1, "name": "Buddy", "breed": "Golden Retriever", "age": "4 years", "adopted": False},
    {"id": 2, "name": "Rex", "breed": "Bulldog", "age": "6 years", "adopted": False},
    {"id": 3, "name": "Tucker", "breed": "Mixed", "age": "8 months", "adopted": False},
]

@pets_blueprint.route('', methods=['GET'])
def get_pets():
    """Returns all pet data"""
    return jsonify(pets), 200

@pets_blueprint.route('/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """Returns the data of one pet based on the pet_id number"""
    for pet in pets:
        if pet['id'] == pet_id:
            return jsonify(pet), 200
    return jsonify({'message': 'Pet not found'}), 404
