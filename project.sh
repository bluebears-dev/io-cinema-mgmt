#!/usr/bin/env bash

docker-machine start
eval $(docker-machine env)
case $1 in
    "build")
        docker-compose down
        docker-compose build
    ;;
    "test")
        docker-compose exec django true
        if [[ $? -eq 0 ]]
        then
            docker-compose exec django coverage run ./manage.py test
            docker-compose exec django coverage xml
            npm run test
            echo "You can now run sonar-scanner."
        fi
    ;;
    "run")
        docker-compose up postgres django
    ;;
    "rund")
        docker-compose up -d postgres django
    ;;
    "sonar")
        docker-compose up -d sonarqube sonardata
    ;;
    "all")
        docker-compose up -d sonarqube sonardata
        docker-compose up postgres django
    ;;
    "scanner")
        sonar-scanner -D sonar.host.url=http://`docker-machine ip`:9000
    ;;
    "")
        echo "test     Run tests and coverage tools"
        echo "run      Start Django and PostgreSQL service (minimal for app usage)"
        echo "rund     Start Django and PostgreSQL service but detached"
        echo "sonar    Start Sonarqube with database services detached"
        echo "all      Start all services (run and sonar combined)"
        echo "scanner  Run sonar-scanner (coverage files should be available and sonar-scanner installed)"
    ;;
esac
