# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /usr/src/app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Run the scraper when the container launches
CMD ["python", "scraper.py"]
