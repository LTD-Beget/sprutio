#!/bin/bash
set -e

if [ ! -e docker-compose ]; then
    curl -s -L https://github.com/docker/compose/releases/download/1.3.3/docker-compose-Linux-x86_64 -o docker-compose
    chmod +x docker-compose
fi
