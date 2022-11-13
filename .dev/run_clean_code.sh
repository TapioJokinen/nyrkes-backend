#!/bin/sh

docker exec nyrkes_local sh -c 'black --line-length 119 . && isort . && flake8 . && pylint nyrkes/'
docker exec nyrkes_local sh -c 'black --line-length 119 --check . && isort --check --diff . && flake8 . && pylint nyrkes/'
