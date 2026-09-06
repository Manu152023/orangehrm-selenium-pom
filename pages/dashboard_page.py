"""Dashboard Page Object - top nav bar, PIM link, logout."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    PIM_MENU_ITEM = (By.XPATH, "//span[text()='PIM']")
    USER_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    def is_loaded(self):
        return self.is_visible(self.DASHBOARD_HEADER)

    def go_to_pim(self):
        # hover over PIM then click, as required by the workflow
        self.hover(self.PIM_MENU_ITEM)
        self.click(self.PIM_MENU_ITEM)

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)
