import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base URL of the API
BASE_URL = os.getenv("BASE_URL", "https://reqres.in")

# Optional headers (like x-api-key or auth tokens)
DEFAULT_HEADERS = {
    "x-api-key": os.getenv("API_KEY", "reqres-free-v1")
}

# Timeout in seconds for all HTTP requests
REQUEST_TIMEOUT = 10

# Allure environment info (optional)
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")