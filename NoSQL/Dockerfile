# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

WORKDIR /app

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Run apt-get update first
RUN apt-get update

# Install utilities
RUN apt-get install -y curl python3.7 python3-pip

# Install Python packages
RUN pip3 install pymongo==3.10.1

# Copy your Python scripts into the container
COPY . /app

