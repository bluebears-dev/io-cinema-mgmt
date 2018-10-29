# Cinema Management System

## Prerequisites

In order to run development environment you should install:
* Docker + Docker Compose
* Python 3.7
* NodeJS + npm + yarn

## Starting development environment

### Webpack

``` bash
# install all dependencies
yarn

# run webpack dev server
yarn start
```

### Django

``` bash
# install all dependencies
pip install -r requirements.txt

# start django dev server
manage.py runserver
# or
yarn django
```

### PostgreSQL

``` bash
# you should run this as superuser!

docker-compose up
# or in detached mode
docker-compose up -d
```
