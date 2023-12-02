#!/bin/bash

docker build -t fastapi-app -f Dockerfile_fastapi_server .
docker build -t prometheus-server -f Dockerfile_prometheus .
