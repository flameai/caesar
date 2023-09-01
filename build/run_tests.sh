#!/bin/sh

cd source/migrations && alembic upgrade head && cd - && \
pytest