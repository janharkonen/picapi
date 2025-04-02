#!/bin/bash

docker stop picapi-flask
docker rm picapi-flask
cd $(pwd)/API
docker build -t picapi-flask-image .
cd ..
docker run -d -p 5000:5000 --name picapi-flask -v $(pwd)/:/app/ picapi-flask-image
