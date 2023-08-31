import pytest


@pytest.mark.anyio
async def test_root(test_cli):
    response = await test_cli.get("/")
    assert response.status_code == 404
