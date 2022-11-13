#!/bin/sh

docker exec nyrkes_local sh -c 'coverage run manage.py test tests && coverage html && coverage report'
