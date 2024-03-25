#!/bin/sh
poetry shell && \
cd caesar/migrations && alembic upgrade head && cd - && \
pytest
