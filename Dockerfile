FROM python:3.8-slim

COPY ./backend /backend
COPY ./frontend /frontend
COPY requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install python3-dev python3-pip -y \
    && pip3 install -r requirements.txt

ENV PYTHONPATH=/ap
WORKDIR /api

EXPOSE $PORT