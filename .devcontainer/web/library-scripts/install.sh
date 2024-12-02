#!/bin/bash
DOCKER_VERSION=23.0.1
DOCKER_BUILDX_VERSION=0.10.3

## install docker buildx
wget https://github.com/docker/buildx/releases/download/v$DOCKER_BUILDX_VERSION/buildx-v$DOCKER_BUILDX_VERSION.linux-amd64 -O /tmp/docker-buildx
mkdir -p /usr/lib/docker/cli-plugins/
install /tmp/docker-buildx /usr/lib/docker/cli-plugins/

## Clean up
rm -rf /tmp/docker*

npm config set strict-ssl=false

