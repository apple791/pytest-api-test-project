# 设置 Cookie
# ↓
# 访问 cookies 接口
# ↓
# 断言服务端确实收到了 Cookie


import pytest
from common.yaml_util import load_case_data, get_case_ids
from common.request_util import send_get_request
from common.assert_util import assert_session_with_log


case_data = load_case_data("posts_api_cases.yaml")
session_cases = case_data["session_cases"]
session_ids = get_case_ids(session_cases)

@pytest.mark.parametrize(
    "case",
    session_cases,
    ids=session_ids
)
def test_session_save_cookie_from_response(api_session, cookies_url, case):
    cookie_name = case["cookie_name"]
    cookie_value = case["cookie_value"]
    expected = case["expected"]

    set_cookie_url = f"https://httpbin.org/cookies/set/{cookie_name}/{cookie_value}"

    set_response = send_get_request(set_cookie_url, session=api_session, timeout=5)

    assert set_response is not None, "接口请求失败，set_response为None"
    assert set_response.status_code == 200, f"状态码错误：{set_response.status_code}"

    cookies_response = send_get_request(cookies_url, session=api_session, timeout=5)

    assert_session_with_log(cookies_response, expected)








