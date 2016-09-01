#!/bin/bash
set -e

# ignore pushes to non-master branches
if [ "$TRAVIS_PULL_REQUEST" = "false" -a "$TRAVIS_BRANCH" != "master" ]; then
    echo "Skipping build for non-master pushes"
    exit 0
fi

# base python image
docker build -t beget/sprutio-python -f Dockerfile ./

# cron image
docker build -t beget/sprutio-cron -f Dockerfile.cron ./

# rpc image
docker build -t beget/sprutio-rpc -f rpc/Dockerfile rpc/

# app image
docker build -t beget/sprutio-app -f app/Dockerfile app/

# nginx image
docker build -t beget/sprutio-nginx -f Dockerfile.nginx ./

# frontend
docker build -t beget/sprutio-bower -f Dockerfile.bower ./
docker run -v $PWD/app/public:/app -w /app beget/sprutio-bower bower install --allow-root
docker build -t beget/sprutio-frontend -f app/public/Dockerfile app/public/

# EOF
