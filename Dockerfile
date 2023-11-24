# For more information, please refer to https://aka.ms/vscode-docker-python
FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

##### 
## Image Configuration
#####

ENV PYTHON_VERSION=3.9.14
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


# Install dev dependencies

RUN apt update && \
    apt install -y git

# # Install python
RUN mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -y --no-install-recommends wget gradle \
    build-essential libgraphviz-dev tar zlib1g-dev libffi-dev libreadline-dev \
    libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev \
    liblzma-dev p7zip-full wget git
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
    tar -xf Python-${PYTHON_VERSION}.tar.xz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make -j 4 && \
    make install && \
    ln -s /usr/local/bin/python3 /usr/bin/python && \
    ln -s /usr/local/bin/pip3 /usr/bin/pip

##### 
## Application Setup
#####

WORKDIR /mcpp
COPY . /mcpp

RUN pip install -e .
