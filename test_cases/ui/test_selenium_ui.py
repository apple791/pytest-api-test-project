# Selenium UI 自动化测试：填写官方 Web Form 并校验提交结果
import json

import allure
import pytest

from pages.web_form_page import WebFormPage
from common.yaml_util import load_case_data, get_case_ids

case_data = load_case_data("ui_cases.yaml")
web_form_cases = case_data["web_form_cases"]
case_ids = get_case_ids(web_form_cases)

pytestmark = pytest.mark.ui

@allure.feature("UI 自动化测试")
@allure.story("Selenium 官方表单提交")
@allure.title("{case[case_name]}")
@pytest.mark.parametrize(
    "case",
    web_form_cases,
    ids=case_ids
)
def test_selenium_web_form(browser, case):
    page = WebFormPage(browser)

    input_text = case["input_text"]
    expected_message = case["expected_message"]

    with allure.step("打开 Selenium 官方 Web Form 页面"):
        page.open()

    with allure.step("校验页面标题"):
        assert "Web form" in page.get_title()

    with allure.step("准备测试数据"):
        allure.attach(
            json.dumps(case, ensure_ascii=False, indent=2),
            name="测试数据",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("填写表单文本"):
        page.fill_text(input_text)

    with allure.step("校验输入框内容"):
        actual_input_text = page.get_input_value()

        if input_text:
            assert actual_input_text == input_text, (
                f"输入内容错误，期望：{input_text}，实际：{actual_input_text}"
            )

        else:
            assert actual_input_text == "", (
                f"空字符串输入失败，实际：{actual_input_text}"
            )

    with allure.step("提交表单"):
        page.submit()

    with allure.step("校验提交结果"):
        actual_message = page.get_message()

        assert actual_message == expected_message, (
            f"提交结果错误，期望：{expected_message}，实际：{actual_message}"
        )









