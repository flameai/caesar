FROM python:3.11-alpine3.17

WORKDIR /app

COPY ./source/requirements.txt .

RUN apk update && \
    apk add --no-cache --virtual .build-deps git && \
    pip install -r ./requirements.txt && \
    apk del .build-deps

COPY . .