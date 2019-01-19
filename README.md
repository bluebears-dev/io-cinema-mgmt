# Cinema Management System

## Installation
### Prerequisites

    python3 + pip
    Oracle VM VirtualBox
    docker
    docker-compose
    docker-machine
    nodejs
    npm

Installation of above packages might differ greatly depending on which platform you are using. Please refer to the installation guides on the internet.

If you are using Windows, please install Docker Toolbox instead of separate Docker components.
Setup

Before starting to setup this environment, please ensure you are in project path and all prerequisites are install. If not all prerequisites are install you might need to install them during the whole process.

You will have to also make your own .env file which will contain specific information like: username, password, host and port for database connection. Please use the template file .env.example in order to create it. Depending on your setup HOST might take values like 127.0.0.1, 192.168.99.100 or something simillar. Please do NOT use PORT value equal to 8080 and 8000 as they are both reserved for webpack and Django respectively. Not following this advice might result in failure to run your project!
### Full-docker setup

First, we have to create Docker machine using VirtualBox driver. It is used because of the Docker Toolbox usage on Windows (Hyper-V is not available on Home or Education Windows editions).

```bash
# create machine 'default' using virtualbox driver
$ docker-machine create default --driver virtualbox
$ docker-machine stop default

# make current working directory shared to VM
$ vboxmanage sharedfolder add default --name "io" --hostpath "${PWD}" --automount
$ docker-machine start default
$ eval $(docker-machine env default)
```
Depending on platform PWD might be an empty string or vboxmanage command might not be available on PATH. If this occurs on your system, please provide path manually to both project directory and vboxmanage binary.

After setting up your docker machine, you will need to install npm packages and build containers. Containers are also built the first time you use docker-compose up command.
```bash
$ docker-compose build
$ npm install
```
#### Running project

Running project will consist of few steps:
```bash
# you might need to start docker machine before you use this command
# sudo might be needed if the setup of docker machine was done on the root
$ ./project.sh run

# start webpack static files server
$ npm run dev
```
Then connect with IP address from Django instance, NOT webpack server IP address.
### Alternative setup

The above setup with shared filesystem for Django might not work on every machine - most of the time it is Docker and VirtualBox issues.

We can then run Django without container on virtualenv and PostgreSQL on docker container without a shared filesystem.

There is also a possibility to create the virtual environment for Python in PyCharm directly. If you decide to do it using PyCharm IDE, please refer to the internet as it is out of the scope of this guide.
```bash
# create virtual environment for Python
$ virtualenv ./venv
# this step might differ on different platforms
# please refer to virtualenv documentation on how to activate it
$ source ./venv/bin/activate
(venv) $ pip install -r requirements.txt

$ docker-compose build postgres
$ npm install
```
#### Running project

Running project will consist of few steps:
```bash
# run PostgreSQL
$ docker-compose up postgres
# run Django
$ source ./venv/bin/activate
(venv) $ python manage.py runserver
# run webpack
$ npm run dev
```
### Making migrations and loading data
After setting up project your database will be empty and there is no way to log into Django admin panel.
Firstly you'll have to make migrations, migrate and load everything into database.
```bash
# make sure you refer to your cinema docker-machine
eval $(docker-machine env '<machine_name>')
# make migrations and migrate
docker-compose exec django python manage.py makemigrations
docker-compose exec django python manage.py migrate
# load placeholder data
docker-compose exec django python manage.py loaddata <available_fixtures>
```
Last command will depend on whether you will want to import all prepared fixtures or some of them.
List of currently available fixtures:
    
    auth - Authentication data, permission groups, admin account (admin:administrator)
    cinema - Cinema data, rooms and their layouts
    content - Movies
    movie_genre - All popular movie genres
    ticket_type - Default ticket types

Some of those fixtures are depending on others. Please be advised that all fixtures are prepared in Polish language.
### Sonarqube

To start Sonarqube simply run `./project.sh sonar`. After few seconds of booting up service will be available 
on **http://<your-docker-machine-ip>:9000/**. Using **admin:admin** as username and password will let you login.

#### Sonar Scanner

Running static code analysis will require you to have `sonar-scanner` installed locally. 
Please refer to Sonarqube documentation on how to install it properly.

## Environment variables

`POSTGRES_USER` - username to login into PotgreSQL

`POSTGRES_PASSWORD` - password to login into PotgreSQL

`POSTGRES_DB` - name of database in PostgreSQL to use

`DATABASE_URL` - URL or IP of PostgreSQL

`DATABASE_PORT` - port of PostgreSQL

`HOST` - URL or IP of hosted application

## Tests

If project is set up properly then running `./project.sh test` 
will start Python and Vue unit tests. It will also generate coverage files inside `/coverage` folder. 

Right now, to start end-to-end test you'll have to do it manually.