#!/bin/bash -x

set -e

rm -rf layer
docker build -t n12-awssdk-builder .
CONTAINER=$(docker run -d n12-awssdk-builder false)
docker cp $CONTAINER:/opt layer
docker rm $CONTAINER
