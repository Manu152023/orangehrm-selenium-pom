"""Base Page - common helper methods shared by all Page Objects."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
