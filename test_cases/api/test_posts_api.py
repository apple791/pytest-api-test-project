# 文章接口基础测试：创建文章、按用户 ID 查询文章列表
import json
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

    with allure.step("准备请求数据"):
        allure.attach(
            json.dumps(payload, ensure_ascii=False, indent=2),
            name="请求数据",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("发送 POST 请求"):
        response = send_post_request(posts_url, payload=payload)

        if response is not None:
            allure.attach(
                response.text,
                name="响应内容",
                attachment_type=allure.attachment_type.JSON
            )

    with allure.step("校验响应结果"):
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

    with allure.step("准备请求数据"):
        allure.attach(
            json.dumps(params, ensure_ascii=False, indent=2),
            name="查询参数",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("发送 GET 请求"):
        list_response = send_get_request(posts_url, params=params)

        if list_response is not None:
            allure.attach(
                list_response.text,
                name="响应内容",
                attachment_type=allure.attachment_type.JSON
            )

    with allure.step("校验响应结果"):
        assert_with_log(
            assert_get_posts_by_user_id_response,
            list_response,
            expected
        )




