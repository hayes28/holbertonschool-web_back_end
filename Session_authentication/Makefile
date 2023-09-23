.PHONY: install run clean

#Build docker image
build:
	docker build -t basic_auth .

# Run docker container Tasks with code hot-reloading, debug, and development environment
run:
	docker run --name Tasks -p 5000:5000 -e API_HOST=0.0.0.0 \
	-e API_PORT=5000 \
	-e AUTH_TYPE=$(AUTH_TYPE) \
	-e FLASK_ENV=development \
	-e FLASK_DEBUG=1 -v $(PWD):/app basic_auth

# Run docker container Tasks in background
start:
	docker start Tasks

# Install dependencies
install:
	pip3 install -r requirements.txt

# Stop container Tasks
stop:
	docker stop Tasks

# Stop all running docker containers
stopall:
	docker stop $$(docker ps -a -q)

# Remove container Tasks
remove:
	docker rm Tasks

# Logs container Tasks
logs:
	docker logs Tasks

# Shell container Tasks
shell:
	docker exec -it Tasks /bin/bash

# Clean all pycache
clean:
	find . -name "*.pyc" -exec rm {} \;
