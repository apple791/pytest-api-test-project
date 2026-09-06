# 文章接口流程测试：查询文章列表后提取第一篇文章 ID，再查询文章详情
import pytest
from common.request_util import send_get_request
from common.assert_util import assert_posts_list_response, assert_post_detail_response, assert_with_log
from common.yaml_util import load_case_data, get_case_ids

pytestmark = pytest.mark.flow

case_data = load_case_data("posts_api_cases.yaml")
flow_cases = case_data["flow_cases"]
flow_ids = get_case_ids(flow_cases)

@pytest.mark.parametrize(
    "case",
    flow_cases,
    ids=flow_ids
)
def test_get_post_detail_by_list_first_id(posts_url, case):

    params = case["params"]
    expected = case["expected"]
    list_response = send_get_request(posts_url, params=params)

    first_post = assert_with_log(
        assert_posts_list_response,
        list_response,
        expected_user_id=expected["userId"],
        expected=expected
    )

    post_id = first_post["id"]

    detail_url = posts_url + f"/{post_id}"

    detail_response = send_get_request(detail_url)

    assert_with_log(
        assert_post_detail_response,
        detail_response,
        expected_post_id=post_id,
        expected=expected
    )
