"""PIM Page Object - PIM landing page with Add Employee / Employee List tabs."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PimPage(BasePage):
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[contains(.,'Add Employee')]")
    EMPLOYEE_LIST_MENU_ITEM = (By.XPATH, "//a[contains(@href,'viewEmployeeList')]")

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def go_to_employee_list(self):
        self.click(self.EMPLOYEE_LIST_MENU_ITEM)
