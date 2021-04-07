#!/bin/bash -x

set -e

rm -rf layer
docker build -t n12-mqtt-builder .
CONTAINER=$(docker run -d n12-mqtt-builder false)
docker cp $CONTAINER:/opt layer
docker rm $CONTAINER
