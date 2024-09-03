# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY anonimize_test.py .
COPY input.csv /app/input.csv
COPY anonymized_data.csv /app/anonymized_data.csv

# Copy requirements.txt if you have additional dependencies
# Uncomment the following two lines if you have a requirements.txt
# COPY requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Install any necessary Python packages
# This is where you can add additional packages if needed
# RUN pip install --no-cache-dir pandas  # Example for additional package

# Command to run the script
CMD ["python", "anonimize_test.py"]
