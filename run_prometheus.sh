#!/bin/bash

docker rm prometheus
docker run -p 9090:9090 --name prometheus prometheus-server
