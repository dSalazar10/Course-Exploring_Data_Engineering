#!/usr/bin/env bash

# Set docker path name and tag
MASTER="dsalazar10/cassandra:master"

# Run master image
docker run -it --rm --name cassandra-node1 -p7000:7000 -p7001:7001 -p9042:9042 -p9160:9160 $MASTER
