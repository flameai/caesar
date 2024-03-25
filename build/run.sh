#!/bin/sh
cd caesar/migrations && alembic upgrade head && cd - && \
python -m caesar.app
