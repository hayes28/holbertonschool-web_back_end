# Start from Ubuntu 18.04 base image
FROM ubuntu:18.04

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install the required dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs

# Working directory
WORKDIR /app

# Copy files to the image
# COPY . .
# Added commands to my Makefile

# Install dependencies
RUN npm install

# Expose port 1245
EXPOSE 1245

# Run command when the container starts
# CMD ["node", "0-console.js"]
# Added commands to my Makefile
