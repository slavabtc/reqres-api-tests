from data.payloads import valid_login, invalid_login

def test_successful_login(api):
    response = api.post("/api/login", json=valid_login)
    assert response.status_code == 200
    assert "token" in response.json()

def test_unsuccessful_login(api):
    response = api.post("/api/login", json=invalid_login)
    assert response.status_code == 400
    assert "error" in response.json()