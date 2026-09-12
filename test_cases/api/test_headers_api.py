# Headers 测试：发送自定义请求头，并校验服务端是否收到
import pytest
from common.request_util import send_get_request
from common.assert_util import assert_headers_response
from common.yaml_util import load_case_data, get_case_ids

pytestmark = pytest.mark.headers

case_data = load_case_data("posts_api_cases.yaml")
headers_cases = case_data["headers_cases"]
headers_ids = get_case_ids(headers_cases)

@pytest.mark.parametrize(
    "case",
    headers_cases,
    ids = headers_ids
)
def test_send_custom_headers(headers_url, case):
    headers = case["headers"]
    expected = case["expected"]

    response = send_get_request(headers_url, headers=headers)

    assert_headers_response(response, expected)