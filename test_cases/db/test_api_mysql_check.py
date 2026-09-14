# 接口与 MySQL 联合校验测试。
import json
import allure
import pytest

from common.mysql_util import query_mysql
from common.request_util import send_get_request
from common.yaml_util import load_case_data, get_case_ids

pytestmark = pytest.mark.api_mysql

case_data = load_case_data("posts_api_cases.yaml")
api_mysql_cases = case_data["api_mysql_cases"]
case_ids = get_case_ids(api_mysql_cases)

@allure.feature("接口与数据库联合校验")
@allure.story("接口用户与 MySQL 用户一致性")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    api_mysql_cases,
    ids=case_ids
)
def test_get_posts_and_mysql_user_consistency(posts_url, case):
    params = case["params"]
    expected = case["expected"]
    expected_user_id = params["userId"]

    with allure.step("发送文章查询请求"):
        response = send_get_request(
            posts_url,
            params=params
        )

        if response is not None:
            allure.attach(
                response.text,
                name="接口响应",
                attachment_type=allure.attachment_type.JSON
            )

    with allure.step("校验接口响应"):
        assert response is not None, "接口请求失败，response 为 None"
        assert response.status_code == expected["status_code"], (
            f"状态码错误，实际：{response.status_code}"
        )

    with allure.step("校验接口文章数据"):
        posts = response.json()

        assert isinstance(posts, list)

        if expected.get("expect_posts", True):
            assert posts

            for post in posts:
                assert post["userId"] == expected_user_id
        else:
            assert posts == []

    sql = """
        select id, name, phone
        from users 
        where id = %s
    """

    with allure.step("查询 MySQL 用户数据"):
        users = query_mysql(sql, (expected_user_id,))

        allure.attach(
            json.dumps(users, ensure_ascii=False, default=str, indent=2),
            name="MySQL 查询结果",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("校验 MySQL 用户数据"):
        if expected["db_user_exists"]:
            assert len(users) == 1
            assert users[0]["id"] == expected_user_id
            assert users[0]["name"] == expected["user_name"]
            assert users[0]["phone"] == expected["user_phone"]
        else:
            assert len(users) == 0
            #或 assert not users
