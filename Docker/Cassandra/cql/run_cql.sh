#!/usr/bin/env bash

# Set docker path name and tag
CQL="dsalazar10/databases:cql"

# Run container
docker run -it --rm -e CQLSH_HOST=$(docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-node1) --name cassandra-client --entrypoint=cqlsh $CQL