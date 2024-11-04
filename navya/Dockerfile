# Start from a base Python image
FROM python:3.10

# Set the working directory to the root of the project
WORKDIR /app

# Copy all project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
