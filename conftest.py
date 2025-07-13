import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api():
    return APIClient(base_url="https://reqres.in")