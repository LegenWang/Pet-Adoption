from flask import Flask '''main.py that routes the methods in the files'''

# Import your API blueprints
from test import test_blueprint
from pets import pets_blueprint


app = Flask(__name__)


# Register blueprints
app.register_blueprint(test_blueprint, url_prefix='/test')
app.register_blueprint(pets_blueprint, url_prefix='/pets')


@app.route('/')
def index():
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)
