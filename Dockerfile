# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy everything in the current directory (host machine) to /usr/src/app (container)
COPY . .

# Install necessary dependencies
RUN pip install beautifulsoup4 requests pandas

# Run scraper.py when the container launches
CMD ["python", "./scraper.py"]
