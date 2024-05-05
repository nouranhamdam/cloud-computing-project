# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install build dependencies and MySQL client libraries
RUN apt-get update \
    && apt-get install -y build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Specify the command to run on container start
CMD [ "python", "app.py" ]
