import pytest
from utils.api_client import APIClient
from config import config

@pytest.fixture(scope="session")
def api():
    return APIClient(base_url=config.BASE_URL, headers=config.DEFAULT_HEADERS)