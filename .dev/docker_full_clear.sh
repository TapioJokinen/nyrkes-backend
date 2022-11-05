#!/bin/sh

echo "Stopping containers..."
docker stop "$(docker ps -a -q)"

echo "Running docker system prune..."
docker system prune -a -f

echo "Removing all containers..."
docker rm "$(docker ps -a -q)"

echo "Removing all images..."
docker rmi "$(docker images -a -q)"

echo "Removing all volumes..."
docker volume prune -f
