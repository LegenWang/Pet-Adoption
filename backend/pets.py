'''Pet API file'''
import sqlite3
from flask import jsonify, Blueprint
from flasgger import Swagger

pets_blueprint = Blueprint('pets', __name__)

swagger = Swagger()

@pets_blueprint.route('/', methods=['GET'])
def get_pets():
    """
    Returns all pet data from the database, including image URLs.
    ---
    tags:
      - Pets
    responses:
      200:
        description: List of pets
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "Buddy"
              species:
                type: string
                example: "Dog"
              age:
                type: integer
                example: 3
              image_url:
                type: string
                example: "/static/images/pets/1.jpg"
      500:
        description: Server error
    """
    conn = sqlite3.connect('petSite.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Pets")
    pets = cursor.fetchall()

    # Convert rows to a list of dictionaries and add the image URL
    pet_list = [
        {**dict(pet)}
        for pet in pets
    ]
    conn.close()
    return jsonify(pet_list), 200


@pets_blueprint.route('/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """
    Returns a single pet data by ID from the database, including the image URL.
    ---
    tags:
      - Pets
    parameters:
      - name: pet_id
        in: path
        required: true
        type: integer
        description: The ID of the pet to fetch
    responses:
      200:
        description: Pet data
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: "Buddy"
            species:
              type: string
              example: "Dog"
            age:
              type: integer
              example: 3
            image_url:
              type: string
              example: "/static/images/pets/1.jpg"
      404:
        description: Pet not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Pet not found"
    """
    conn = sqlite3.connect('petSite.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Pets WHERE id = ?", (pet_id,))
    pet = cursor.fetchone()
    conn.close()

    if pet is None:
        return jsonify({'error': 'Pet not found'}), 404

    # Convert the pet row to a dictionary and add the image URL
    pet_data = dict(pet)
  
    return jsonify(pet_data), 200
