FROM python:3.11-alpine3.17

WORKDIR /app

COPY ./source/requirements.txt .

RUN apk update && \
    apk add --virtual .build_deps git && \
    pip install -r ./requirements.txt && \
    apk del .build_deps

COPY . .