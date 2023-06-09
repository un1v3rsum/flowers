FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /flowers_app

ADD . /flowers_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /flowers_app


