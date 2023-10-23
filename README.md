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
2) Dockerfile (https://docs.docker.com/engine/reference/builder/)
3) requirements.txt (https://pip.pypa.io/en/stable/reference/requirements-file-format/)

![image](https://github.com/jaezeu/hello-flask/assets/48310743/7ddb7999-988c-4c01-ad94-65729f17e78a)


You may have to run the commands below in sudo if your user is not in a docker user group. To run docker as a non root user: https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user

```
# Build a docker image locally
docker build -t flask-app .

# Listing your built images
docker images

# Starting your local container with port mapping
docker run -d -p 8080:8080 flask-app

# List all your containers(Running and stopped)
docker ps -a

# To stop and remove your container
docker stop <container ID>
docker rm <container ID>

# To remove your docker images
docker rmi <image ID>

```
