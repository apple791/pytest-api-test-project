import os
import allure
from datetime import datetime
import pytest
import requests
from config.config import BASE_URL, HEADERS_URL, BEARER_URL, COOKIES_URL
from common.db_util import init_demo_db
from selenium import webdriver

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


# 初始化 SQLite测试数据库
@pytest.fixture
def init_db():
    init_demo_db()


# 创建浏览器实例，用于Selenium UI自动化测试
@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name.replace("/", "_")
        screenshot_path = (
            f"reports/screenshots/{test_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{test_name}_失败截图",
            attachment_type=allure.attachment_type.PNG
        )

        allure.attach(
            driver.page_source,
            name=f"{test_name}_页面源码",
            attachment_type=allure.attachment_type.HTML
        )

        print(f"失败截图已保存：{screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call",report)

