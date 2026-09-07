# 文章接口基础测试：创建文章、按用户 ID 查询文章列表
import allure
import pytest
from common.request_util import send_get_request, send_post_request
from common.yaml_util import load_case_data
from common.case_util import build_pytest_params
from common.assert_util import (
    assert_create_post_response,
    assert_get_posts_by_user_id_response,
    assert_with_log
)

case_data = load_case_data("posts_api_cases.yaml")

post_cases = case_data["post_cases"]
get_cases = case_data["get_cases"]

post_params = build_pytest_params(post_cases)
get_params = build_pytest_params(get_cases)

@allure.feature("文章接口")
@allure.story("创建文章")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    post_params
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

@allure.feature("文章接口")
@allure.story("根据用户 ID 查询文章列表")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    get_params
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



