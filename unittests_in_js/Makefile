# Build the docker image
build:
	docker build --no-cache -t unittestjs .

# Run the docker container with volume
run:
	docker run -d -t --name unittestjs-container -p 7865:7865 -v $(PWD):/app unittestjs

# Start the docker container
start:
	docker start unittestjs-container

# Stop the docker container
stop:
	docker stop unittestjs-container

# Copy files to the running container
copy:
	docker cp . unittestjs-container:/app

# Run the tests
test:
	docker exec -it unittestjs-container npm run test *.test.js

# Open a shell inside the running container
shell:
	docker exec -it unittestjs-container /bin/bash
