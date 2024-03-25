FROM python:3.12-alpine3.17

ENV PATH=$PATH:/root/.local/bin/
WORKDIR /app

COPY pyproject.toml .

RUN apk update && \
    apk add --no-cache --virtual .build-deps git gcc musl-dev curl && \
    curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false && \
    poetry install && \
    apk del .build-deps

COPY ./src .
COPY ./build/run.sh .
