#!/usr/bin/env bash

# Set docker path name and tag
DOCKERPATH="dsalazar10/airflow"

# Run node image
docker run -d -p 8080:8080 $DOCKERPATH webserver
