#!/usr/bin/env bash

docker-compose exec django coverage run ./manage.py test
docker-compose exec django coverage xml
