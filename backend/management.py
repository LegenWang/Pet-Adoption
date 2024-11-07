"""management"""
import sqlite3
from flask import request, jsonify, Blueprint
from flasgger import Swagger

swagger = Swagger()
application_blueprint = Blueprint("application", __name__)

@application_blueprint.route('/', methods=['GET'])
def get_applications():
    """
    Retrieve all applications
    This endpoint returns a list of all applications stored in the database.
    ---
    tags:
      - Applications
    responses:
      200:
        description: A list of applications
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
                example: John Doe
              status:
                type: string
                example: Pending
    """
    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Applications")
    rows = cursor.fetchall()
    applications = [dict(row) for row in rows]
    return jsonify(applications)

@application_blueprint.route('/<int:app_id>', methods=['GET'])
def get_application(app_id):
    """
    Retrieve an application by ID
    This endpoint retrieves a specific application by its ID.
    ---
    tags:
      - Applications
    parameters:
      - name: app_id
        in: path
        type: integer
        required: true
        description: ID of the application to retrieve
    responses:
      200:
        description: An application object
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: John Doe
            status:
              type: string
              example: Approved
      404:
        description: Application not found
    """
    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Applications WHERE id = ?", (app_id,))
    application = cursor.fetchone()

    connection.close()

    if application is None:
        return jsonify({"message": "Application not found"}), 404
    return jsonify(dict(application))

@application_blueprint.route('/manage_login', methods=['POST'])
def manage_login():
    """
    Authenticate a manager
    This endpoint authenticates a manager using their email and password.
    ---
    tags:
      - Manager Authentication
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            manager_email:
              type: string
              example: manager@example.com
            manager_password:
              type: string
              example: password123
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            message:
              type: string
              example: Login successful
            manager_email:
              type: string
              example: manager@example.com
      401:
        description: Invalid manager email or password
    """
    data = request.get_json()

    manager_email = data.get("manager_email")
    manager_password = data.get("manager_password")

    connection = sqlite3.connect('petSite.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Managers WHERE manager_email = ? AND manager_password = ?", 
                   (manager_email, manager_password))
    manager = cursor.fetchone()

    connection.close()

    if manager is None:
        return jsonify({"message": "Invalid manager email or password"}), 401

    return jsonify({"message": "Login successful", "manager_email": manager["manager_email"]}), 200

# Ensure to initialize Swagger in your main app entry file:
# from flask import Flask
# from flasgger import Swagger
# from your_module import application_blueprint

# app = Flask(__name__)
# Swagger(app)
# app.register_blueprint(application_blueprint, url_prefix='/applications')

# if __name__ == '__main__':
#     app.run(debug=True)
