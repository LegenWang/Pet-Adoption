''' API File '''
import sqlite3
from flask import Blueprint, request, jsonify
from flasgger import Swagger

user_blueprint = Blueprint('user', __name__)

swagger = Swagger()

@user_blueprint.route('/login', methods=['POST'])
def login_users():
    ''' 
    Log in a user by verifying their username and password 

    This endpoint allows users to log in by providing their username and password.

    ---
    tags:
      - Users
    parameters:
      - name: username
        in: body
        required: true
        type: string
        description: The username of the user.
      - name: password
        in: body
        required: true
        type: string
        description: The password of the user.
    responses:
      200:
        description: User logged in successfully.
        schema:
          type: object
          properties:
            username:
              type: string
              example: "john_doe"
      401:
        description: Invalid username or password.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Invalid username or password"
    '''
    credentials = request.json
    username = credentials.get("username")
    password = credentials.get("password")

    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    connection.close()

    if user is None:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"username": user["username"]}), 200


@user_blueprint.route('/register', methods=['POST'])

def register_user():
    ''' 
    Register a new user with a unique username and password

    This endpoint allows new users to register by providing a unique username and a password.

    ---
    tags:
      - Users
    parameters:
      - name: username
        in: body
        required: true
        type: string
        description: The username for the new user.
      - name: password
        in: body
        required: true
        type: string
        description: The password for the new user.
    responses:
      201:
        description: User registered successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User registered successfully"
      400:
        description: Username already exists.
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Username already exists"
    '''
    user_data = request.json
    username = user_data.get("username")

    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        connection.close()
        return jsonify({"error": "Username already exists"}), 400

    cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)",
     (username, user_data.get("password")))
    connection.commit()
    connection.close()

    return jsonify({"message": "User registered successfully"}), 201

# log out is commented because in the app we can either ues a session or
# jwt token to manage logged in users
# @user_blueprint.route('/logout', methods=['POST'])
# def logout_user():
#     ''' Log out a user '''
#     credentials = request.json
#     username = credentials.get("username")

#     if username in logged_in_users:
#         logged_in_users.remove(username)
#         return jsonify({"message": "User logged out successfully"}), 200
#     return jsonify({"error": "User is not logged in"}), 404
