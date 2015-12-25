#!/bin/bash
set -e

REQUIRED_VERSION=${1:-1.6.0}

function version2int {
    printf "%03d%03d%03d%03d" $(echo "$1" | tr '.' ' ')
}

DOCKER=$(which docker 2>/dev/null)

if [ -z "$DOCKER" ]; then
    echo "Docker Engine ${REQUIRED_VERSION} or later is required to run SprutIO"
    echo "Please follow https://docs.docker.com/linux/ to install Docker Engine"
    exit 1
fi

DOCKER_VERSION=$(docker version -f '{{.Server.Version}}' 2>/dev/null || docker version | perl -ne 'm/Server:?\s*[vV]ersion: (\S+)/ && print $1')

if [ $(version2int $DOCKER_VERSION) -lt $(version2int $REQUIRED_VERSION) ]; then
    echo "Docker Engine ${REQUIRED_VERSION} or later is required to run SprutIO"
    echo "Please upgrade your Docker Engine to run SprutIO"
    exit 1
fi

