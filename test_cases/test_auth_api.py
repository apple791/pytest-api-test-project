# 鉴权失败场景
import os
import pytest
from common.request_util import send_get_request
from common.yaml_util import load_case_data
from common.assert_util import assert_bearer_response

# current_dir = os.path.dirname(__file__)
# project_root = os.path.dirname(current_dir)
# case_file = os.path.join(project_root, "data", "posts_api_cases.yaml")

case_data = load_case_data("posts_api_cases.yaml")
#?这句是不是不用写
assert case_data is not None, "YAML文件为空或读取失败"
bearer_cases = case_data["bearer_cases"]
# 这句是不是可以调用get_case_ids
bearer_ids = [case["case_name"] for case in bearer_cases]

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




