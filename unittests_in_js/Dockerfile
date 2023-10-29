# Use the official Ubuntu 18.04 base image.
FROM ubuntu:18.04

# Set environment variables to non-interactive.
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies.
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory.
WORKDIR /app

# Copy package files and install npm packages.
COPY package*.json ./
RUN npm install

# Copy all files.
COPY . .
