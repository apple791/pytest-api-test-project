# 查询用户文章列表并查看第一篇详情
import os
import pytest
from common.request_util import send_get_request
from common.assert_util import assert_posts_list_response, assert_post_detail_response, assert_with_log
from common.yaml_util import load_yaml

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
case_file = os.path.join(project_root,"data","posts_api_cases.yaml")

case_data = load_yaml(case_file)
assert case_data is not None, "YAML文件为空或读取失败"
flow_cases = case_data["flow_cases"]
flow_ids = [case["case_name"] for case in flow_cases]

@pytest.mark.parametrize("case", flow_cases, ids=flow_ids)
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
