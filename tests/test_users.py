from schemas.user_schema import user_list_schema
from utils.schema_validator import validate_schema

def test_get_users(api):
    response = api.get("/api/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0

def test_get_single_user(api):
    response = api.get("/api/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_user_not_found(api):
    response = api.get("/api/users/23")
    assert response.status_code == 404

def test_create_user(api):
    payload = {
        "name": "Morpheus",
        "job": "Leader"
    }
    response = api.post("/api/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data and "createdAt" in data

def test_update_user(api):
    payload = {
        "name": "Neo",
        "job": "The One"
    }
    response = api.put("/api/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Neo"

def test_delete_user(api):
    response = api.delete("/api/users/2")
    assert response.status_code == 204

def test_user_list_schema(api):
    response = api.get("/api/users?page=2")
    assert response.status_code == 200
    validate_schema(response.json(), user_list_schema)

def test_create_user_with_empty_payload(api):
    response = api.post("/api/users", json={})
    assert response.status_code == 201  # ReqRes allows it but test what happens
    assert "id" in response.json()
