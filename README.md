# Flask server app on docker

This project is very minimal but show how to use docker to build a flask server.

- we use some library to show how to use the requirement.txt file
- we output a file to show how to use binding volumes 

## To run this project 
`git clone https://github.com/nynif/docker_flask.git`  
`cd docker_flask`

#### docker running version
`docker compose up`

*On your local machine, the output file will be in app_local/app/output/ folder*


#### local running version
`python -m venv .env`  
`source .env/bin/activate`  
`pip install -r app_local/requirements.txt`  
`python -m flask --app app_local/app.py run`

*The output file will be in app/output/ folder*

# Source
- https://github.com/docker/awesome-compose/tree/master/flask
- https://youtu.be/gAGEar5HQoU
- https://hub.docker.com/_/python