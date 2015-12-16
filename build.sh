#!/bin/bash
set -e
source docker-compose.sh
exec ./docker-compose -f build.yml build

