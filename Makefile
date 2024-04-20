# A makefile for Docker commands

# variables
IMAGE_NAME := anomaly-image
CONTAINER_NAME := anomaly-container
DATA_PATH := $(shell pwd)/data
NOTEBOOKS_PATH := $(shell pwd)/notebooks
PORT := 8888

.PHONY: build run logs stop clean

# Build the docker image
build:
	docker build -t $(IMAGE_NAME) ./docker

# run the docker container
run:
	docker run -d \
		-v $(DATA_PATH):/data \
		-v $(NOTEBOOKS_PATH):/notebooks \
		-p $(PORT):8888 \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)
	@echo "Container $(CONTAINER_NAME) started."
	@echo "Fetching Notebook URL:"
	@sleep 4
	@make logs

logs:
	docker logs $(CONTAINER_NAME)

# stop the Docker container
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)

# Stop and remove the container, then remove the image
purge: stop clean
