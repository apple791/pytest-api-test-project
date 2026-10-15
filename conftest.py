import os
from datetime import datetime
from pathlib import Path

import allure
import pytest
import requests
from selenium import webdriver

from common.db_util import init_demo_db
from config.config import (
    BASE_URL,
    HEADERS_URL,
    BEARER_URL,
    COOKIES_URL,
    REQUEST_TIMEOUT,
)


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


# 提供统一的接口请求超时时间
@pytest.fixture
def request_timeout():
    return REQUEST_TIMEOUT


# 创建独立 Session，用于测试 Cookie 自动保存和携带
@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()


# 初始化 SQLite 测试数据库
@pytest.fixture
def init_db(tmp_path):
    db_path = tmp_path / "demo.db"
    init_demo_db(db_path)
    return db_path


# 创建浏览器实例，用于 Selenium UI 自动化测试
@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    try:
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
    finally:
        driver.quit()


# pytest 测试结果钩子：记录测试执行结果，供失败截图和 Allure 附件使用
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call", report)



def pytest_addoption(parser):
    parser.addoption("--run-mysql", action="store_true", help="运行已配置的本地MySQL练习")
    parser.addoption("--run-ui", action="store_true", help="运行需要Chrome的UI练习")
    parser.addoption("--headless", action="store_true", help="Chrome使用无界面模式")


def pytest_collection_modifyitems(config, items):
    for item in items:
        if (item.get_closest_marker("mysql") or item.get_closest_marker("api_mysql")) and not config.getoption("--run-mysql"):
            item.add_marker(pytest.mark.skip(reason="MySQL练习需配置测试库并传入--run-mysql"))
        if item.get_closest_marker("ui") and not config.getoption("--run-ui"):
            item.add_marker(pytest.mark.skip(reason="UI练习需安装Chrome并传入--run-ui"))
