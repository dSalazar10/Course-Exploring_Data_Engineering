#!/usr/bin/env bash

# Set docker path name and tag
NODE="dsalazar10/cassandra:node"

# Run node image
docker run -it --rm --name cassandra-node2 -p27000:7000 -p27001:7001 -p29042:9042 -p29160:9160  -e CASSANDRA_SEEDS="$(docker inspect --format='{{ .NetworkSettings.IPAddress }}' cassandra-node1)" $NODE
# Once in shell, enter the following command:
docker exec -it cassandra-node2 /docker-entrypoint.sh cassandra -f
