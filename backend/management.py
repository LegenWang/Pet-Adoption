"""
Unit tests for the management module, including tests for application retrieval 
and manager login functionality.
"""
from flask import request, jsonify, Blueprint

application_blueprint = Blueprint("application", __name__)

# Sample data for testing purposes
applications = [
    {"id": 1, "user_name": "Alice", "user_age": "30", "user_occupation": "Engineer",
     "user_salary": "80000", "pet_name": "Buddy", "pet_breed": "Golden Retriever"},
    {"id": 2, "user_name": "Bob", "user_age": "40", "user_occupation": "Teacher",
     "user_salary": "50000", "pet_name": "Rex", "pet_breed": "Bulldog"}
]

managers = [
    {"id": 1, "manager_email": "admin@example.com", "manager_password": "password123"}
]

@application_blueprint.route('/', methods=['GET'])
def get_applications():
    """Returns a list of all applications."""
    return jsonify(applications)

@application_blueprint.route('/<int:app_id>', methods=['GET'])
def get_application(app_id):
    """Returns a specific application by ID, or 404 if not found."""
    for application in applications:
        if application['id'] == app_id:
            return jsonify(application)
    return '<h1>Application not found</h1>', 404

@application_blueprint.route('/manage_login', methods=['POST'])
def manage_login():
    """Authenticates a manager using email and password."""
    data = request.get_json()
    manager_email = data.get("manager_email")
    manager_password = data.get("manager_password")

    # Check for manager credentials in the sample data
    for manager in managers:
        if manager["manager_email"] == manager_email:
            if manager["manager_password"] == manager_password:
                return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401
