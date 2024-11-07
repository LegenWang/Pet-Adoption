"""module docstring"""
from flask import Flask
from flasgger import Swagger
# Import your API blueprints
from pets import pets_blueprint
from users import user_blueprint
from management import application_blueprint
app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

# Register blueprints
app.register_blueprint(pets_blueprint, url_prefix='/pets')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(application_blueprint, url_prefix='/application')



@app.route('/')
def index():
    """function docstring"""
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)
