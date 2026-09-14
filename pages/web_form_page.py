"""
Selenium Web Form 页面对象。

封装 Selenium 官方 Web Form 页面的常用操作，包括：

- 打开 Web Form 页面；
- 填写文本；
- 点击提交按钮；
- 获取输入框内容；
- 获取提交后的提示信息。
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class WebFormPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    TEXT_INPUT = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE = (By.ID, "message")

    def open(self):
        self.open_url(self.URL)

    def fill_text(self, text):
        self.input_text(self.TEXT_INPUT, text)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_message(self):
        return self.get_text(self.MESSAGE)

    def get_input_value(self):
        element = self.wait_visible(self.TEXT_INPUT)
        return element.get_attribute("value")


