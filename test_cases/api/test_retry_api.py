# 请求重试测试：验证请求异常或指定状态码时的重试机制
import allure
import pytest
from common.yaml_util import load_case_data, get_case_ids
from common.request_util import send_get_request_with_retry

pytestmark = pytest.mark.retry

case_data = load_case_data("posts_api_cases.yaml")
retry_cases = case_data["retry_cases"]
retry_ids = get_case_ids(retry_cases)

@allure.feature("请求封装")
@allure.story("请求重试机制")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    retry_cases,
    ids=retry_ids
)
def test_get_with_retry_by_yaml(case):
    url = case["url"]
    retry_times = case["retry_times"]
    retry_status_codes = case["retry_status_codes"]
    expected = case["expected"]

    response = send_get_request_with_retry(
        url=url,
        retry_times=retry_times,
        retry_status_codes=retry_status_codes
    )

    assert response is not None, "接口请求失败，response为None"
    assert response.status_code == expected["status_code"], f"状态码错误：{response.status_code}"




