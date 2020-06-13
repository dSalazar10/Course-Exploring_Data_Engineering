#!/bin/bash

# Be sure to execute this command with the following:
# . ./upload_docker.sh

FOLDERS=("master" "node" "cql")
WDIR=$PWD
#echo "Working directory = ${WDIR}"
for FOLDER in ${FOLDERS[@]}
do
    #echo "Changing to ${FOLDER} dir:"
    cd $FOLDER
    #echo "Uploading..."
    ./upload_docker.sh
    cd $WDIR
done