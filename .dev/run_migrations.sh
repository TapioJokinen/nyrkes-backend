#!/bin/sh

docker exec -it nyrkes_local sh -c 'python manage.py makemigrations && python manage.py migrate'
