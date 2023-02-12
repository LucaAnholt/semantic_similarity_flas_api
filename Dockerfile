# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the image
COPY requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the image
COPY index.py /app

# Set the environment variable for Flask
ENV FLASK_APP=index.py

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
