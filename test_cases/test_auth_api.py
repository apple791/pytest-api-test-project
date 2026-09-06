# Bearer Token 鉴权测试：覆盖携带 Token 成功和未携带 Token 失败场景
import pytest
from common.request_util import send_get_request
from common.yaml_util import load_case_data, get_case_ids
from common.assert_util import assert_bearer_response

pytestmark = pytest.mark.auth

case_data = load_case_data("posts_api_cases.yaml")
bearer_cases = case_data["bearer_cases"]
bearer_ids = get_case_ids(bearer_cases)

@pytest.mark.parametrize(
    "case",
    bearer_cases,
    ids=bearer_ids
)
def test_bearer_token(bearer_url,case):
    headers = case["headers"]
    expected = case["expected"]

    response = send_get_request(bearer_url, headers=headers)

    assert_bearer_response(response, expected)




