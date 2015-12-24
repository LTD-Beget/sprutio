#!/bin/bash
set -e

source docker-version.sh 1.7.1
source docker-compose.sh 1.5.2

if ! docker inspect beget/sprutio-python >&/dev/null; then
    make build-python
fi

export COMPOSE_HTTP_TIMEOUT=300

COMPOSE_CMD="./docker-compose-1.5.2 -p sprutio -f docker-compose.yml -f docker-compose.dev.yml"

if [ $# -eq 0 ]; then
    exec ${COMPOSE_CMD} up -d
else
    exec ${COMPOSE_CMD} "$@"
fi

# EOF
