# Anamoly Detection Project

## Context

This is a small docker project that is meant to build and run an anomaly detection algorithm on sample data

I've used Makefile instead of docker-compose here to get more practice with the docker commands themselves

### How To Run Notebook

To build and run the docker container:

```make
make build && make run_notebook
```

To stop the docker container

```make
make stop_notebook
```

### How to Run Service

To build and run the docker container:

```make
make build && make run_service
```

To stop the docker container

```make
make stop_service
```

## Sample cURL commands

cURL commands as output from FastAPI

```zsh
# score = false
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction?score=false' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  0.1, 0.1
]'


# score = true
curl -X 'POST' \
  'http://0.0.0.0:8000/prediction?score=true' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  0.1, 0.1
]'


# GET command
curl -X 'GET' \
  'http://0.0.0.0:8000/model_information' \
  -H 'accept: application/json'
```
