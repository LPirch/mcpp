# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

##### 
## Image Configuration
#####

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# switch default shell from /bin/sh to /bin/bash to be able to use source
SHELL ["/bin/bash", "-c"]

##### 
## Tool Setup
#####

# Install system dependencies

RUN apt update && \
    apt install -y git

##### 
## Application Setup
#####

WORKDIR /mcpp
COPY . /mcpp

RUN pip install -e .
