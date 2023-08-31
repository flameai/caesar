from fastapi.testclient import TestClient
import pytest
from httpx import AsyncClient

from source.app import app
from common.fastapi.settings import APP_HOST, APP_PROTO


@pytest.mark.anyio
@pytest.fixture
async def test_cli():
    async with AsyncClient(app=app, base_url=f"{APP_PROTO}://{APP_HOST}") as cli:
        yield cli
