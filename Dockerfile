FROM python:3.10.5

RUN apt-get -y install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
