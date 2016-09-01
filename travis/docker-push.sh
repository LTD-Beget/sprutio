#!/bin/bash
set -e

# ignore pull requests
if [ "$TRAVIS_PULL_REQUEST" != "false"  ]; then
    echo "Skipping push for pull requests"
    exit 0
fi

# ignore non-master branches
if [ "$TRAVIS_BRANCH" != "master" ]; then
    echo "Skipping push for non-master branches"
    exit 0
fi

# login to docker hub
docker login --email=$DOCKER_HUB_EMAIL --username=$DOCKER_HUB_USERNAME --password=$DOCKER_HUB_PASSWORD

# push release images
docker push beget/sprutio-cron
docker push beget/sprutio-rpc
docker push beget/sprutio-app
docker push beget/sprutio-nginx
docker push beget/sprutio-frontend

# EOF
