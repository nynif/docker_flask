# Minimal version of a flask server app on docker

This project is very minimal but show how to use docker to build a flask server.

Some point :
- we use some library to show how to use the requirement.txt file
- we output a file to show how to use binding volumes 

# To run this project 
`git clone`

## docker quick version
`docker compose up`

## docker detail version
`docker build -t my_image_name
docker run -p 5000:5000 -d -v ./app_local:/app my_image_name`

## local version
`python -m venv .env
source .env/bin/activate
pip install -r app_local/requirements.txt
python -m flask run
`

# Source
- https://github.com/docker/awesome-compose/tree/master/flask
- https://youtu.be/gAGEar5HQoU
- https://hub.docker.com/_/python


