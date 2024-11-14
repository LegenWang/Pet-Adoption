Instructions to run frontend Docker container
Run this command to create the image for Team46 backend
docker build --tag react-team46 .
Run the Docker container on port 5173 with this command
docker run -p 5173:5173 react-team46
