from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def wait_clickable(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        return element

    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

