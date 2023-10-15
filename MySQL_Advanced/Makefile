.PHONY: install run clean

# Build the Docker image
build:
	docker build -t mysql-docker .

# Run the Docker container
run:
	docker run -d -t --name mysql-container -p 3306:3306 mysql-docker

# Run docker container in background
start:
	docker start mysql-container

# Start MySQL service in the running container
start_mysql:
	docker exec -it mysql-container service mysql start

# Stop the Docker container
stop:
	docker stop mysql-container

# Stop all running docker containers
stopall:
	docker stop $$(docker ps -a -q)

# Remove the Docker image
remove:
	docker rmi mysql-docker

# Logs container mysql
logs:
	docker logs mysql-container

# Shell container mysql
shell:
	docker exec -it mysql-container /bin/bash

# Remove the Docker container
clean:
	docker rm mysql-container

# Connect to MySQL inside the container
connect:
	docker exec -it mysql-container mysql -uroot -proot

# Import SQL files
import:
	cat ./sql_scripts/*.sql | docker exec -i mysql-container mysql -uroot -proot my_database
