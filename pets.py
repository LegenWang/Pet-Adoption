from flask import jsonify, Blueprint '''import modules'''
pets_blueprint = Blueprint("pets", __name__)

pets = [
    {"id": 1, "name": "Buddy", "breed": "Golden Retriever", "age": "4 years", "adopted": False},
    {"id": 2, "name": "Rex", "breed": "Bulldog", "age": "6 years", "adopted": False},
    {"id": 3, "name": "Tucker", "breed": "Mixed", "age": "8 months", "adopted": False},
]

@pets_blueprint.route('', methods=['GET'])
def get_pets():
    return jsonify(pets)

@pets_blueprint.route('/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    for pet in pets:
        if pet['id'] == pet_id:
            return jsonify(pet)
    return '<h1>Pet not found</h1>'
