def test_root(test_cli):
    response = test_cli.get("/")
    assert response.status_code == 404
