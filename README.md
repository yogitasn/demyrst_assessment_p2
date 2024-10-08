# demyrst_assessment_p2

## Problem2: Data processing
- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform


## Project Name
# Overview
This project utilizes Docker to build and run a containerized application for data processing of csv file to anonymise the data. The following steps outline how to build the Docker image, execute the container, and interact with it.

## 1. Anonymizing Data with hashlib

We'll use hashlib to hash the sensitive columns (first_name, last_name, and address) to anonymize them. Hashing will replace the sensitive data with a hashed version that maintains privacy.

## 2. Using Distributed Computing with concurrent.futures

We'll use Python’s concurrent.futures to process the data in parallel. This approach will work for larger files by splitting the processing workload across multiple threads.

## Handling Very Large Datasets

For even larger datasets or more complex distributed computing, we can use more advanced frameworks like Apache Spark with PySpark. However, for many cases, using concurrent.futures as shown will be efficient and straightforward for handling large files with distributed processing.

This approach ensures that sensitive information is anonymized securely using hashing and processes the data efficiently using parallel processing.

## Prerequisites
Docker installed on your machine
Basic understanding of Docker commands

## Steps to build Docker Image
# 1. Build the Docker Image

To build the Docker image for data parsing, use the following command:

``` docker build -t anonimize_test . ```

This command builds the Docker image and tags it as parser_clean

## 2. Run the Docker Container for Data Parsing

After building the image, you can run the Docker container to perform the data parsing. Use the following command:

``` docker run --rm -v C:/demyrst_assessment_p2/input.csv:/app/input.csv -v C:/demyrst_assessment_p2/anonymized_data.csv:/app/anonymized_data.csv anonimize_test ``` 

Here's what this command does:

* --rm: Automatically removes the container after it exits.
* -v C:/demyrst_assessment_p2/input.csv:/app/input.csv: Mounts the local input.csv file to the container.
* -v C:/demyrst_assessment_p2/anonymized_data.csv:/app/anonymized_data.csv: Mounts the local anonymized_data.csv file to the container.
anonimize_test: Specifies the image to use.

## 3. Access an Interactive Python Environment (Optional)

If you need to interact with the container or debug, you can start an interactive shell session:

``` docker run -it --rm -v C:/demyrst_assessment_p2:/app python:3.9-slim /bin/bash ```

This command does the following:

* -it: Runs the container in interactive mode with a terminal.
* --rm: Automatically removes the container after you exit.
* -v C:/demyrst_assessment_p2:/app: Mounts the local directory to the container.
* python:3.9-slim: Uses the official Python 3.9 slim image.
* /bin/bash: Starts a bash shell inside the container.

## Files Involved
* input.csv: Input data file.
* anonymized_data.csv: Output file where the anonymized data will be written.

## Notes
* Ensure Docker is installed and running on your machine before executing these commands.
* `anonymized_data.csv` starts as an empty file. On a local machine, the Python script automatically creates and writes to this file. However, when running the script inside a Docker container, the file is not created automatically. Therefore, you need to manually create an empty `anonymized_data.csv` file before running the script in the Docker container. The script will then write the results to this file as expected. Please refer to the screenshot for the output results in the file.
* Adjust file paths (C:/demyrst_assessment_p2/) according to your local setup.
* Using --rm ensures that the container is cleaned up after execution, which helps in managing disk space and container clutter.

## Troubleshooting
If you encounter issues, verify the following:

* Docker installation and configuration are correct.
* File paths are correct and accessible.
* The Docker image builds and runs without errors.

For further assistance, consult the Docker documentation or review the Dockerfile and any related scripts included in the project.