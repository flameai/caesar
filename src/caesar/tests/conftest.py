import pytest
from fastapi.testclient import TestClient

from common.fastapi.registry import get_db

from caesar.models import Group
from caesar.app import app


@pytest.fixture
def test_cli():
    with TestClient(app) as client:
        yield client


@pytest.fixture
async def db_session():
    return get_db()


@pytest.fixture
async def initial_data():
    group1 = Group(name="admins")
    group2 = Group(name="users")

    data = []
    data.append(group1)
    data.append(group2)

    return data


@pytest.fixture
async def fill_and_clear_db(db_session):
    pass
