from schemas.user_schema import user_list_schema
from utils.schema_validator import validate_schema

def test_get_users(api):
    response = api.get("/api/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0

def test_get_existing_user(api):
    response = api.get("/api/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2

def test_get_nonexistent_user(api):
    response = api.get("/api/users/999")
    assert response.status_code == 404

def test_create_user(api):
    payload = {
        "name": "Ihor",
        "job": "QA Engineer"
    }
    response = api.post("/api/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data and "createdAt" in data

def test_update_user(api):
    payload = {
        "name": "Updated Ihor",
        "job": "Senior QA"
    }
    response = api.put("/api/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_delete_user(api):
    response = api.delete("/api/users/2")
    assert response.status_code == 204
    assert response.text == ""


def test_user_list_schema(api):
    response = api.get("/api/users?page=2")
    assert response.status_code == 200
    validate_schema(response.json(), user_list_schema)

def test_create_user_with_empty_payload(api):
    response = api.post("/api/users", json={})
    assert response.status_code == 201  # ReqRes allows it but test what happens
    assert "id" in response.json()

def test_partial_update_user(api):
    partial_payload = {
        "job": "Lead QA Engineer"
    }

    response = api.patch("/api/users/2", json=partial_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == partial_payload["job"]
    assert "updatedAt" in data
