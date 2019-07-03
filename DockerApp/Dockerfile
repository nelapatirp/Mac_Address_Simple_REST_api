# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /macapp
WORKDIR /macapp

# Copy the current directory contents into the container at /macapp
COPY . /macapp

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80


# Run macapp.py when the container launches
CMD ["python", "macapp.py"]
