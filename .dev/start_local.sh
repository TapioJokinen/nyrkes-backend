#!/bin/sh

docker-compose -f docker-compose.local.yml down

if [ $# -eq 0 ]; then
    docker-compose -f docker-compose.local.yml up
fi

if [ "$1" = "-b" ] || [ "$1" = "-B" ]; then
    docker-compose -f docker-compose.local.yml build --build-arg VERSION="$TAG"
    docker-compose -f docker-compose.local.yml up
fi
