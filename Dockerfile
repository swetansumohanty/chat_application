FROM python:3 

ENV PYTHONUNBUFFERED 1

WORKDIR /demo-app

ADD . /demo-app

COPY ./requirements.txt /demo-app/requirements.txt

RUN pip install -r requirements.txt

COPY . /demo-app