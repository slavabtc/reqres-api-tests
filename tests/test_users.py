import allure
from schemas.user_schema import user_list_schema
from utils.schema_validator import validate_schema


@allure.feature("Users")
@allure.story("List users")
@allure.title("Verify user list endpoint returns data")
def test_get_users(api):
    with allure.step("Send GET request to fetch users"):
        response = api.get("/api/users?page=2")
    with allure.step("Assert response code and data"):
        assert response.status_code == 200
        assert "data" in response.json()
        assert len(response.json()["data"]) > 0


@allure.feature("Users")
@allure.story("Get single user")
@allure.title("Verify existing user can be retrieved")
def test_get_existing_user(api):
    response = api.get("/api/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2


@allure.feature("Users")
@allure.story("Get single user")
@allure.title("Verify 404 for non-existent user")
@allure.severity(allure.severity_level.NORMAL)
def test_get_nonexistent_user(api):
    response = api.get("/api/users/999")
    assert response.status_code == 404


@allure.feature("Users")
@allure.story("Create user")
@allure.title("Verify user can be created")
def test_create_user(api):
    payload = {"name": "Ihor", "job": "QA Engineer"}
    response = api.post("/api/users", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data and "createdAt" in data


@allure.feature("Users")
@allure.story("Update user")
@allure.title("Verify full update with PUT")
def test_update_user(api):
    payload = {"name": "Updated Ihor", "job": "Senior QA"}
    response = api.put("/api/users/2", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data


@allure.feature("Users")
@allure.story("Delete user")
@allure.title("Verify user can be deleted")
def test_delete_user(api):
    response = api.delete("/api/users/2")
    assert response.status_code == 204
    assert response.text == ""


@allure.feature("Users")
@allure.story("Schema validation")
@allure.title("Validate user list response against schema")
def test_user_list_schema(api):
    response = api.get("/api/users?page=2")
    assert response.status_code == 200
    validate_schema(response.json(), user_list_schema)


@allure.feature("Users")
@allure.story("Create user")
@allure.title("Verify behavior when creating user with empty payload")
@allure.severity(allure.severity_level.MINOR)
def test_create_user_with_empty_payload(api):
    response = api.post("/api/users", json={})
    assert response.status_code == 201
    assert "id" in response.json()


@allure.feature("Users")
@allure.story("Partial update")
@allure.title("Verify PATCH updates part of user data")
@allure.severity(allure.severity_level.CRITICAL)
def test_partial_update_user(api):
    partial_payload = {"job": "Lead QA Engineer"}
    response = api.patch("/api/users/2", json=partial_payload)
    data = response.json()
    assert response.status_code == 200
    assert data["job"] == partial_payload["job"]
    assert "updatedAt" in data