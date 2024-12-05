''' API File '''
import sqlite3
import os
from functools import wraps
import requests
import jwt
from jwt.exceptions import PyJWTError
from functools import wraps
from flask import Blueprint, request, jsonify, Flask
from flasgger import Swagger

user_blueprint = Blueprint('users', __name__)
app = Flask(__name__)
swagger = Swagger(app)

@app.after_request
def after_request(response):
    '''
    Add headers to enable CORS
    '''
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

def verify_token(f):
    '''
    Decorator to verify Auth0 JWT token
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization header is missing"}), 401
        
        try:
            # Remove 'Bearer ' from the header
            token = auth_header.split(' ')[1]
            
            # Fetch JWKS (JSON Web Key Set) from Auth0
            domain = "dev-pwaee0xegp145q52.us.auth0.com"  # Replace with your Auth0 domain
            jwks_url = f'https://{domain}/.well-known/jwks.json'
            
            # Fetch JWKS
            jwks_response = requests.get(jwks_url)
            jwks = jwks_response.json()
            
            # Find the right key for the token
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            for key in jwks['keys']:
                if key['kid'] == unverified_header['kid']:
                    rsa_key = {
                        'kty': key['kty'],
                        'kid': key['kid'],
                        'use': key['use'],
                        'n': key['n'],
                        'e': key['e']
                    }
            
            if not rsa_key:
                return jsonify({"error": "Unable to find appropriate key"}), 401

            # Verify the token
            payload = jwt.decode(
                token, 
                rsa_key, 
                algorithms=['RS256'], 
                audience="https://dev-pwaee0xegp145q52.us.auth0.com/api/v2/",  # Replace with your Auth0 API identifier
                options={"verify_aud": False}
            )
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except PyJWTError:
            return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            return jsonify({"error": "Authentication failed", "details": str(e)}), 401
        
        return f(*args, **kwargs)
    return decorated_function

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

    connection = sqlite3.connect('users_managers.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Check if it's a manager login
    cursor.execute("SELECT * FROM Managers WHERE manager_email = ? AND manager_password = ?",
     (username, password))
    manager = cursor.fetchone()

    # If manager is found, return hardcoded role 'manager'
    if manager:
        return jsonify({
            "message": f"Welcome back, {manager['manager_email']}!",
            "role": "manager"
        }), 200

    # Check if it's a user login
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    connection.close()

    if user is None:
        return jsonify({"error": "Invalid username/email or password"}), 401

    return jsonify({
        "message": f"Welcome back, {user['username']}!",
        "role": user['role']
    }), 200


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
    email = user_data.get("email")
    password = user_data.get("password")

    connection = sqlite3.connect('users_managers.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Check if the username or email already exists
    cursor.execute("SELECT * FROM Users WHERE username = ? OR email = ?", (username, email))
    existing_user = cursor.fetchone()

    if existing_user:
        connection.close()
        return jsonify({"error": "Username or email already exists"}), 400

    cursor.execute("INSERT INTO Users (username, email, password) VALUES (?, ?, ?)",
    (username, email, password))
    connection.commit()
    connection.close()

    return jsonify({"message": "User registered successfully"}), 201

@user_blueprint.route('/all', methods=['GET'])
@verify_token
def get_all_users():
    """
    Fetch all users from the database.

    This endpoint retrieves a list of all registered users and their details.

    ---
    tags:
      - Users
    responses:
      200:
        description: A list of all users.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: "john_doe"
              email:
                type: string
                example: "john_doe@example.com"
      500:
        description: Database error.
    """
    connection = sqlite3.connect('users_managers.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT id, username, email FROM Users")
    users = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return jsonify(users), 200

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
