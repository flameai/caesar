def test_root(test_cli):
    response = test_cli.post("/api/v1/membership/1")

    assert response.status_code == 200
