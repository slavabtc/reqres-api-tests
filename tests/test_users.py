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