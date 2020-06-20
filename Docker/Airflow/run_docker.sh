#!/usr/bin/env bash

# Set docker path name and tag
DOCKERPATH="dsalazar10/airflow"

# Run node image
docker run -d -p 8080:8080 -v /Users/doopyduper/Documents/DevOps/Course-Exploring_Data_Engineering/Docker/Airflow/volume/airflow/dags:/usr/local/airflow/dags $DOCKERPATH webserver
