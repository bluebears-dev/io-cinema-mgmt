#!/usr/bin/env bash

eval $(docker-machine env)
docker-compose exec django coverage run ./manage.py test
docker-compose exec django coverage xml

echo "You can run now 'sonar-scanner -D sonar.host.url=http://`docker-machine ip`:9000/'"