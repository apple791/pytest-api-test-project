# 接口与 SQLite 数据库联合校验测试。
import allure
import pytest
from common.request_util import send_get_request
from common.db_util import query_db
from common.yaml_util import load_case_data, get_case_ids

pytestmark = pytest.mark.api_db

case_data = load_case_data("posts_api_cases.yaml")
api_db_cases = case_data["api_db_cases"]
api_db_ids = get_case_ids(api_db_cases)

@allure.feature("接口与数据库校验")
@allure.story("接口返回用户与数据库用户一致性校验")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    api_db_cases,
    ids=api_db_ids
)
def test_get_posts_user_exists_in_db(posts_url, case, init_db):
    params = case["params"]
    expected = case["expected"]

    response = send_get_request(posts_url, params=params)

    assert response is not None
    assert response.status_code == expected["status_code"]

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    user_id = data[0]["userId"]

    sql = "select * from users where id = ?"
    db_users = query_db(sql, (user_id,))

    if expected["db_user_exists"]:
        assert len(db_users) == 1
        assert db_users[0]["id"] == user_id
    else:
        assert len(db_users) == 0


