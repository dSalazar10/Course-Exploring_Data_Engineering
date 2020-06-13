#!/usr/bin/env bash

# Set docker path name and tag
DOCKERPATH="dsalazar10/postgres"

# Run container
docker run -it -p 5432:5432 --rm -e POSTGRES_PASSWORD=PassWord123 $DOCKERPATH 
