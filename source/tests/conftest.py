import pytest
from fastapi.testclient import TestClient

from source.app import app


@pytest.fixture
def test_cli():
    with TestClient(app) as client:
        yield client
