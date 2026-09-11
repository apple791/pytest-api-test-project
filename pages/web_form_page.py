from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebFormPage:
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    TEXT_INPUT = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def input_text(self, text):
        text_input = self.wait.until(
            EC.visibility_of_element_located(self.TEXT_INPUT)
        )
        text_input.clear()
        text_input.send_keys(text)

    def submit(self):
        submit_button = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        submit_button.click()

    def submit_text(self, text):
        self.input_text(text)
        self.submit()

    def get_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        )
        return message.text


