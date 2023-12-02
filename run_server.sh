#!/bin/bash

docker rm fastapi_server
docker run -p 8000:8000 --name fastapi_server fastapi-app
