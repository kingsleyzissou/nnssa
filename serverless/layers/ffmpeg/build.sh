#!/bin/bash -x

set -e

rm -rf layer
docker build -t py37-ffmpeg-builder .
CONTAINER=$(docker run -d py37-ffmpeg-builder false)
docker cp $CONTAINER:/opt layer
docker rm $CONTAINER
