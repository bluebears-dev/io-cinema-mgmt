FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./docker/wait.sh .
RUN chmod 777 wait.sh
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN cd / &&\
    apt-get update &&\
    apt-get install wget &&\
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz &&\
    tar vxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz &&\
    cp wkhtmltox/bin/wk* /usr/local/bin/