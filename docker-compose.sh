#!/bin/bash
set -e

VERSION=${1:-1.3.3}

if [ ! -e docker-compose-$VERSION ]; then
    curl -s -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-Linux-x86_64 -o docker-compose-${VERSION}
    chmod +x docker-compose-${VERSION}
fi
