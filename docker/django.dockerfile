FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./docker/wait.sh .
RUN chmod 777 wait.sh
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install wkhtmltopdf
