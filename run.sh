#!/bin/bash

docker-machine start
docker-machine env
eval $(docker-machine env)
docker-compose up
