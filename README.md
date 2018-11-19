# Cinema Management System

## Prerequisites

### Linux

Install:
* python3 + pip
* Oracle VM VirtualBox
* docker
* docker-compose
* docker-machine
* nodejs
* npm

Installation of above packages might differ throughout distributions.

**On Ubuntu:**
```bash
# install docker
apt-get install docker.io

# install docker-compose
pip install docker-compose

# install docker-machine
curl -L https://github.com/docker/machine/releases/download/v0.3.0/docker-machine_linux-amd64 > /usr/local/bin/docker-machine
chmod +x /usr/local/bin/docker-machine

# install nodejs and npm
apt-get install nodejs npm
```

Now we will create new docker machine that uses VirtualBox as it's VM driver:
```bash
cd /path/to/project

# create machine 'default' using virtualbox driver
docker-machine create default --driver virtualbox
docker-machine stop default

# make current working directory shared to VM
vboxmanage sharedfolder add default --name "io" --hostpath "${PWD}" --automount
docker-machine start default
docker-machine env default
```


## Starting development environment

### Webpack

``` bash
# install all dependencies
npm install

# run webpack dev server
npm run dev
```

### Django 

``` bash
# install all dependencies
pip install -r requirements.txt

# start django dev server
manage.py runserver
# or
npm run django
```

### PostgreSQL

``` bash
# you should run this as superuser!

docker-compose up
# or in detached mode
docker-compose up -d
```
