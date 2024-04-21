# A makefile for Docker commands

# variables
IMAGE_NAME := anomaly-image
IMAGE_SERVICE_NAME := fastapi-image
CONTAINER_NAME := anomaly-container
SERVICE_NAME := fastapi-service
DATA_PATH := $(shell pwd)/data
NOTEBOOKS_PATH := $(shell pwd)/notebooks
PORT := 8888
PORT_SERVICE := 8000

.PHONY: build run_notebook run_service logs stop_service stop_notebook clean

# Build the docker image
build:
	docker build -t $(IMAGE_NAME) ./docker/
	docker build -t $(IMAGE_SERVICE_NAME) ./service/

# run the docker container
run_notebook:
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

run_service:
	docker run -d \
		-v $(DATA_PATH):/data \
		-p $(PORT_SERVICE):8000 \
		--name $(SERVICE_NAME) \
		${IMAGE_SERVICE_NAME}

# stop the Docker container
stop_notebook:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

stop_service:
	docker stop $(SERVICE_NAME)
	docker rm $(SERVICE_NAME)

# remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)
	docker rmi $(IMAGE_SERVICE_NAME)

# Stop and remove the container, then remove the image
purge: stop_notebook stop_service clean
