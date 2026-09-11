# Selenium UI 自动化测试：填写官方 Web Form 并校验提交结果
import allure
import pytest
from pages.web_form_page import WebFormPage

pytestmark = pytest.mark.ui

@allure.feature("UI自动化测试")
@allure.story("Selenium官方表单提交")
@allure.title("填写Web Form并校验提交结果")
def test_selenium_web_form(browser):
    page = WebFormPage(browser)

    with allure.step("打开 Selenium 官方 Web Form 页面"):
        page.open()

    with allure.step("填写文本并提交表单"):
        page.submit_text("pytest selenium")

    with allure.step("校验提交成功提示"):
        assert page.get_message() == "Received!"







