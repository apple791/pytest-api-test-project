# Bearer Token 鉴权测试：覆盖携带 Token 成功和未携带 Token 失败场景
import json
import allure
import pytest
from common.request_util import send_get_request
from common.yaml_util import load_case_data, get_case_ids
from common.assert_util import assert_bearer_response

pytestmark = pytest.mark.auth

case_data = load_case_data("posts_api_cases.yaml")
bearer_cases = case_data["bearer_cases"]
bearer_ids = get_case_ids(bearer_cases)

@allure.feature("鉴权接口")
@allure.story("Bearer Token 鉴权")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    bearer_cases,
    ids=bearer_ids
)
def test_bearer_token(bearer_url, case):
    headers = case["headers"]
    expected = case["expected"]

    with allure.step("准备请求头"):
        allure.attach(
            json.dumps(headers, ensure_ascii=False, indent=2),
            name="请求头",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("发送 Bearer 鉴权请求"):
        response = send_get_request(bearer_url, headers=headers)

        if response is not None:
            allure.attach(
                response.text,
                name="响应内容",
                attachment_type=allure.attachment_type.JSON
            )

    with allure.step("校验鉴权响应"):
        assert_bearer_response(response, expected)




