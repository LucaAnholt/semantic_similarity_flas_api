# Use an official Python runtime as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Install the dependencies
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN pip install spacy
RUN python -m spacy download en_core_web_md

# Copy the application code to the image
COPY index.py /app

# Set the environment variable for Flask
ENV FLASK_APP=index.py

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
