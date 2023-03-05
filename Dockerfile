# Use the official Python image as the base image
FROM python:3.10

WORKDIR /code

COPY requirements.txt /code

# Install the application dependencies
RUN pip install -r /code/requirements.txt

COPY . /code

EXPOSE 5000

# Define the entry point for the container
CMD ["python", "main.py"]
