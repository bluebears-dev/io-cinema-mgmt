#!/usr/bin/env bash

eval $(docker-machine env)
docker-compose exec django coverage run ./manage.py test
docker-compose exec django coverage xml
