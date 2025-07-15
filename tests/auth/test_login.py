from data.payloads import valid_login, invalid_login
import pytest

def test_successful_login(api):
    response = api.post("/api/login", json=valid_login)
    assert response.status_code == 200
    assert "token" in response.json()

def test_unsuccessful_login(api):
    response = api.post("/api/login", json=invalid_login)
    assert response.status_code == 400
    assert "error" in response.json()

@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"email": "eve.holt@reqres.in"}, 400),  # missing password
        ({}, 400),                               # missing everything
        ({"email": "", "password": ""}, 400),    # empty strings
    ]
)
def test_invalid_login(api, payload, expected_status):
    response = api.post("/api/login", json=payload)
    assert response.status_code == expected_status