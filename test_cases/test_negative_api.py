import os
import pytest
from common.request_util import send_get_request
from common.yaml_util import load_yaml
from common.assert_util import assert_not_found_response

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
case_file = os.path.join(project_root, "data", "posts_api_cases.yaml")

case_data = load_yaml(case_file)

assert case_data is not None, "YAML文件为空或读取失败"
negative_cases = case_data["negative_cases"]
negative_ids = [case["case_name"] for case in negative_cases]

wrong_path_cases = case_data["wrong_path_cases"]
wrong_path_ids = [case["case_name"] for case in wrong_path_cases]

@pytest.mark.parametrize(
    "case",
    negative_cases,
    ids=negative_ids
)
def test_get_not_exist_post(posts_url, case):

    post_id = case["post_id"]
    expected = case["expected"]

    detail_url = posts_url + f"/{post_id}"

    response = send_get_request(detail_url)

    assert_not_found_response(response, expected)

@pytest.mark.parametrize(
    "case",
    wrong_path_cases,
    ids=wrong_path_ids
)
def test_wrong_api_path(base_url, case):
    wrong_path = case["path"]
    expected = case["expected"]

    wrong_url = base_url + wrong_path

    response = send_get_request(wrong_url)

    assert_not_found_response(response, expected)

