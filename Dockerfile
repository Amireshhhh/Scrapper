# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy everything in the current directory to /usr/src/app
COPY . .

# Install necessary dependencies
RUN pip install beautifulsoup4 requests pandas flask

# Expose the port Flask will run on
EXPOSE 5000

# Run the web server when the container launches
CMD ["python", "app.py"]
