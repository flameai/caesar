import pytest
from fastapi.testclient import TestClient

from common.fastapi.config import ComponentCategoryGetterEnum, get_component

from source.models import Group
from source.app import app


@pytest.fixture
def test_cli():
    with TestClient(app) as client:
        yield client


@pytest.fixture
async def db_session():
    return get_component(ComponentCategoryGetterEnum.RelationalDB)

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