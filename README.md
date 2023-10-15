# py-flask

## Introduction

This repo is used to build a simple hello world flask application and deploy it in a docker environment. The sections below explain on how you can install docker in MacOS / Ubuntu(WSL)

## Docker Installation

### Ubuntu

For those on WSL Ubuntu, follow the instructions(Steps 1 to 3) here to install docker on your WSL terminal: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

### MacOS

For those using MacOS, download docker desktop: https://docs.docker.com/desktop/install/mac-install/

After installing, open your terminal and run the following command to verify that docker is successfully installed:

```
docker --version
```

Remember to launch your Docker Desktop before going to the next section.

## Building and running docker app

Ensure that you have the following 3 files in the directory where you are about to run the commands:

1) app.py
2) Dockerfile
3) requirements.txt

![image](https://github.com/jaezeu/py-flask/assets/48310743/e49e85a5-9905-4348-9b52-8675982abe4b)

```
# Build a docker image locally
sudo docker build -t flask-app .

# Listing your built images
sudo docker images

# Starting your local container with port mapping
sudo docker run -d -p 8080:8080 flask-app

# List all your containers(Running and stopped)
sudo docker ps -a

# To stop and remove your container
sudo docker stop <container ID>
sudo docker rm <container ID>

```
