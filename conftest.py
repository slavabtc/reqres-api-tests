import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api():
    headers = {
        "x-api-key": "reqres-free-v1"
    }
    return APIClient(base_url="https://reqres.in", headers=headers)