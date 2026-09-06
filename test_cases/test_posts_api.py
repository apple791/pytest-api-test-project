import pytest
from common.request_util import send_get_request, send_post_request
from common.yaml_util import load_case_data, get_case_ids
from common.assert_util import (
    assert_create_post_response,
    assert_get_posts_by_user_id_response,
    assert_with_log
)

case_data = load_case_data("posts_api_cases.yaml")

# post_cases 创建文章
post_cases = case_data["post_cases"]
# get_cases 查询文章
get_cases = case_data["get_cases"]
post_ids = get_case_ids(post_cases)
get_ids = get_case_ids(get_cases)

@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    post_cases,
    ids=post_ids
)
def test_create_post(posts_url, case):
    payload = case["payload"]
    expected = case["expected"]

    response = send_post_request(posts_url, payload=payload)

    assert_with_log(
        assert_create_post_response,
        response,
        expected
    )

@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    get_cases,
    ids=get_ids
)
def test_get_posts_by_user_id(posts_url, case):
    params = case["params"]
    expected = case["expected"]

    list_response = send_get_request(posts_url, params=params)

    assert_with_log(
        assert_get_posts_by_user_id_response,
        list_response,
        expected
    )

