"""Add Employee Page Object."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddEmployeePage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast')]")

    def add_employee(self, first_name, last_name):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.click(self.SAVE_BUTTON)
        # wait for redirect to the Personal Details page (URL contains /pim/viewPersonalDetails)
        self.wait.until(lambda d: "viewPersonalDetails" in d.current_url)
