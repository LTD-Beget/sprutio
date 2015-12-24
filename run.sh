#!/bin/bash
set -e

SELF=$(readlink /proc/$$/fd/255)
SELFDIR=$(dirname $SELF)

cd $SELFDIR

REQUIRED="docker-version.sh docker-compose.sh docker-compose.yml app.env rpc.env"
for REQ in $REQUIRED; do
    test -s $REQ || curl -s -L https://raw.githubusercontent.com/LTD-Beget/sprutio/master/$REQ -o $REQ
done

source docker-version.sh 1.6.0
source docker-compose.sh 1.3.3

export COMPOSE_HTTP_TIMEOUT=300

COMPOSE_CMD="./docker-compose-1.3.3 -p sprutio"

if [ $# -eq 0 ]; then
    exec ${COMPOSE_CMD} up -d
else
    exec ${COMPOSE_CMD} "$@"
fi

# EOF
