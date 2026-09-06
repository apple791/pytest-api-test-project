import pytest
import requests
from config.config import BASE_URL, HEADERS_URL, BEARER_URL, COOKIES_URL

# 文章接口地址
@pytest.fixture
def posts_url():
    return BASE_URL + "/posts"

# 项目基础地址
@pytest.fixture
def base_url():
    return BASE_URL

# httpbin headers 测试地址
@pytest.fixture
def headers_url():
    return HEADERS_URL

# httpbin Bearer Token 鉴权测试地址
@pytest.fixture
def bearer_url():
    return BEARER_URL

# httpbin cookies 测试地址
@pytest.fixture
def cookies_url():
    return COOKIES_URL

# 创建独立 Session，用于测试 Cookie 自动保存和携带
@pytest.fixture
def api_session():
    session = requests.Session()
    return session