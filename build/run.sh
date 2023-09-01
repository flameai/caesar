#!/bin/sh

cd source/migrations && alembic upgrade head && cd - && \
python -m source.app