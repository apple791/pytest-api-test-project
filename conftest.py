import pytest
import requests
from config.config import BASE_URL, HEADERS_URL, BEARER_URL, COOKIES_URL

@pytest.fixture
def posts_url():
    return BASE_URL + "/posts"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def headers_url():
    return HEADERS_URL

@pytest.fixture
def bearer_url():
    return BEARER_URL

@pytest.fixture
def cookies_url():
    return COOKIES_URL

@pytest.fixture
def api_session():
    session = requests.Session()
    return session