# @pytest.mark.session
# def test_session_cookie_lifecycle(api_session, cookies_url):
#     set_cookie_url = (
#         f"{cookies_url}/set/session_id/abc123"
#     )
#
#     set_response = api_session.get(set_cookie_url)
#
#     assert set_response.status_code == 200
#     assert api_session.cookies.get("session_id") == "abc123"
#
#     cookies_response = api_session.get(cookies_url)
#
#     assert cookies_response.status_code == 200
#
#     data = cookies_response.json()
#     assert data["cookies"]["session_id"] == "abc123"
#

# import pytest
#
# @pytest.mark.session
# def test_cookie_attributes(api_session, cookies_url):
#     set_cookie_url = f"{cookies_url}/set/session_id/abc123"
#
#     response = api_session.get(
#         set_cookie_url, timeout=5
#     )
#
#     assert response.status_code == 200
#
#     cookies = list(api_session.cookies)
#
#     assert cookies
#
#     cookie = next(
#         item for item in cookies
#         if item.name == "session_id"
#     )
#
#     print("Cookie 名称：", cookie.name)
#     print("Cookie 值：", cookie.value)
#     print("Cookie 域名：", cookie.domain)
#     print("Cookie 路径：", cookie.path)
#     print("Cookie 是否安全传输：", cookie.secure)
#     print("Cookie 过期时间：", cookie.expires)
#
#     assert cookie.name == "session_id"
#     assert cookie.value == "abc123"


# import pytest
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.mark.ui
# def test_selenium_cookie_send_to_server(browser, cookies_url):
#     browser.get(cookies_url)
#
#     browser.add_cookie({
#         "name":"session_id",
#         "value":"abc123",
#         "path":"/"
#     })
#
#     browser.refresh()
#
#     wait = WebDriverWait(browser, 10)
#
#     body = wait.until(
#         EC.visibility_of_element_located((By.TAG_NAME, "body"))
#     )
#
#     assert "session_id" in body.text
#     assert "abc123" in body.text

# import pytest
#
# @pytest.mark.ui
# def test_selenium_cookie_attribtes(browser, cookies_url):
#     browser.get(cookies_url)
#
#     browser.add_cookie({
#         "name": "session_id",
#         "value": "abc123",
#         "path": "/",
#         "secure": True
#     })
#
#     cookie = browser.get_cookie("session_id")
#
#     assert cookie is not None
#
#     print("Cookie 名称：", cookie["name"])
#     print("Cookie 值：", cookie["value"])
#     print("Cookie 路径：", cookie.get("path"))
#     print("Cookie 域名：", cookie.get("domain"))
#     print("Cookie 是否 Secure：", cookie.get("secure"))
#     print("Cookie 是否 HttpOnly：", cookie.get("httpOnly"))
#     print("Cookie SameSite：", cookie.get("sameSite"))
#
#     assert cookie["name"] == "session_id"
#     assert cookie["value"] == "abc123"

# from config.config import BASE_URL, TEST_ENV
#
#
# def test_current_environment():
#     print("当前环境：", TEST_ENV)
#     print("当前接口地址：", BASE_URL)
#
#     assert TEST_ENV in ("dev", "test")
#     assert BASE_URL

from config.config import MYSQL_CONFIG, TEST_ENV


def test_database_environment():
    print("当前环境：", TEST_ENV)
    print("当前数据库：", MYSQL_CONFIG["database"])

    assert TEST_ENV in ("dev", "test")
    assert MYSQL_CONFIG["database"]


