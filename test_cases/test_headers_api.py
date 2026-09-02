import pytest
import os
from common.request_util import send_get_request
from common.assert_util import assert_headers_response
from common.yaml_util import load_yaml

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
case_file = os.path.join(project_root, "data", "posts_api_cases.yaml")

case_data = load_yaml(case_file)
assert case_data is not None, "YAML文件为空或读取失败"
headers_cases = case_data["headers_cases"]
headers_ids = [case["case_name"] for case in headers_cases]

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