# Use Ubuntu 18.04 as base image
FROM ubuntu:18.04

# Set environment variables to non-interactive.
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl build-essential tcl

# Install Node 12.x
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

# COPY Redis 7.2
COPY ./redis-7.2.2.tar.gz /tmp/
RUN tar xzvf /tmp/redis-7.2.2.tar.gz && \
    cd redis-7.2.2 && \
    make && \
    make install


# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json ./

# Install npm packages
RUN npm install

# Copy the entire app
COPY . .

# Expose port 3000 for your app
EXPOSE 1245
