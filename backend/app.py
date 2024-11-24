"""module docstring"""
from flask import Flask
# Import the necessary modules for your blueprints
from pets import pets_blueprint
from users import user_blueprint
from management import application_blueprint
from flasgger import Swagger
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
swagger = Swagger(app)

# Enable CORS for all routes (allowing all origins by default)
CORS(app)  # This enables CORS globally

# If you want to restrict to specific origins, use the following:
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Register blueprints
app.register_blueprint(pets_blueprint, url_prefix='/pets')
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(application_blueprint, url_prefix='/applications')

@app.route('/')
def index():
    """function docstring"""
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)
