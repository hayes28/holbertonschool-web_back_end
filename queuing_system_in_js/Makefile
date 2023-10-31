# Build the docker image
build:
	docker build --no-cache -t queuingjs .

# Run the docker container with volume
run:
	docker run -d -t --name queuingjs-container -p 1245:1245 -v $(PWD):/app queuingjs

# Start the docker container
start:
	docker start queuingjs-container

# Stop the docker container
stop:
	docker stop queuingjs-container

# Copy files to the running container
copy:
	docker cp . queuingjs-container:/app

# Open a shell inside the running container
shell:
	docker exec -it queuingjs-container /bin/bash
