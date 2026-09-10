# Selenium UI 自动化测试：填写官方 Web Form 并校验提交结果
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.ui

def test_selenium_web_form(browser):

    browser.get(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    wait = WebDriverWait(browser, 10)

    text_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "my-text"))
    )

    text_input.send_keys("pytest selenium")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button")

    submit_button.click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Received!"







