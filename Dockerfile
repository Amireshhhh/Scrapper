# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy everything in the current directory to /usr/src/app
COPY . .

# Install necessary dependencies
RUN pip install beautifulsoup4 requests pandas flask

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable (optional)
ENV FLASK_APP=app.py

# Run the Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
