# Use Ubuntu 18.04 as a base image
FROM ubuntu:18.04

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=non-interactive

# Install required packages
RUN apt-get update && \
    apt-get install -y mysql-server-5.7 python3.7 python3-pip && \
    apt-get clean

# Set the MySQL root password
RUN service mysql start && \
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';" && \
    service mysql stop

# Expose MySQL port
EXPOSE 3306

# # Add a startup script
# COPY startup.sh /startup.sh
# RUN chmod +x /startup.sh

# # Run the startup script by default
# CMD ["/startup.sh"]
