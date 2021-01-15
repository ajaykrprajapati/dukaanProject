FROM python:3.8-alpine
 MAINTAINER Ajay Kumar Prajapati

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /dukaan
WORKDIR /dukaan
COPY ./dukaan /dukaan

RUN adduser -D user
User user