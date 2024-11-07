Instructions to run backend Docker container
  Run this command to create the image for Team46 backend
    docker build --tag team46 .
  Run the Docker container on port 5000 with this command
    docker run -d -p 5000:5000 team46
  
Instructions to run the backend server directly (no Docker) on Windows
  cd to the backend folder in your terminal
  Run this command to create a virtual environment in the folder
    py -3 -m venv venv
  Run this command to activate the virtual environment
    venv\Scripts\activate
  Run these commands to install packages used
    pip install flask
    pip install flasgger
  Run this command to run the backend flask app
    python app.py

  API Usage
    Base URL: The backend server is hosted on http://127.0.0.1:5000/
    Swagger Documentation: Once the server is running, access API documentation at http://localhost:5000/apidocs
    Endpoints
    Pets
    GET /pets/: Returns a list of all pets and their information.
    GET /pets/<int:pet_id>: Returns information for a specific pet by pet_id.
    Users
    POST /user/login: Logs in a user with a username and password.
    Example:

    curl -X POST http://127.0.0.1:5000/user/login -H "Content-Type: application/json" -d '{"username":"your_username","password":"your_password"}'
    POST /user/register: Registers a new user with a unique username and password.
    Example:

    curl -X POST http://127.0.0.1:5000/user/register -H "Content-Type: application/json" -d '{"username":"new_user","password":"new_password"}'
    Applications
    GET /application/: Retrieves all applications.
    GET /application/<int:app_id>: Retrieves details of a specific application by app_id.
    Manager Authentication
    POST /application/manage_login: Authenticates a manager with manager_email and manager_password.
    Example
    curl -X POST http://127.0.0.1:5000/application/manage_login -H "Content-Type: application/json" -d '{"manager_email":"manager@example.com","manager_password":"password123"}'
