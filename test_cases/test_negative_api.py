# 异常场景测试：查询不存在的文章 ID，以及请求不存在的接口路径
import pytest
from common.request_util import send_get_request
from common.yaml_util import load_case_data, get_case_ids
from common.assert_util import assert_not_found_response

pytestmark = pytest.mark.negative

data_cases = load_case_data("posts_api_cases.yaml")
negative_cases = data_cases["negative_cases"]
negative_ids = get_case_ids(negative_cases)

wrong_path_cases = data_cases["wrong_path_cases"]
wrong_path_ids = get_case_ids(wrong_path_cases)

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

