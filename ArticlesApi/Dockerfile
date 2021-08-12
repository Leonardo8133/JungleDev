FROM python:3.7-alpine


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps
RUN pip install Django==3.0.7
RUN pip install -r /requirements.txt


RUN mkdir /app
WORKDIR /app
ADD . /app/


