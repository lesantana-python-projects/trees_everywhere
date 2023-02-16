FROM python:3.10.5

ENV C_FORCE_ROOT=1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /code
WORKDIR /code
ADD . /code/

COPY requirements.txt /app
COPY requirements-dev.txt /app

RUN apt-get update
RUN pip install -r requirements-dev.txt --no-cache-dir


EXPOSE 8000
