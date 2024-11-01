''' API File '''
from flask import Blueprint, request, jsonify

user_blueprint = Blueprint('user', __name__)

users = [
    {"username": "steven", "password": "1234567"},
    {"username": "james", "password": "helloworld"}
]
@user_blueprint.route('/login', methods=['POST'])

def login_users():
    ''' Log in a user by verifying their username and password '''
    credentials = request.json
    username = credentials.get("username")
    password = credentials.get("password")

    user = None
    for user_entry in users:
        if user_entry["username"] == username and user_entry["password"] == password:
            user = user_entry
            break

    if user is None:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"username": user["username"]}), 200


@user_blueprint.route('/register', methods=['POST'])

def register_user():
    ''' Register a new user with a unique username and password'''
    user_data = request.json
    username = user_data.get("username")

    for existing_user in users:
        if existing_user["username"] == username:
            return jsonify({"error": "Username already exists"}), 400

    users.append({
        "username": username,
        "password": user_data.get("password")
    })

    return jsonify({"message": "User registered successfully"}), 201
