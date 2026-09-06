"""Employee List Page Object - search, scroll, and verify employee names."""
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EmployeeListPage(BasePage):
    EMPLOYEE_NAME_FILTER = (By.XPATH, "//label[text()='Employee Name']/../../div[2]//input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESULT_ROWS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    EMPLOYEE_NAME_CELLS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[2]/div")

    def search_by_name(self, name):
        self.type_text(self.EMPLOYEE_NAME_FILTER, name)
        self.click(self.SEARCH_BUTTON)

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(1)

    def get_all_employee_names(self):
        """Scrolls through the (paginated) list and collects all visible names."""
        names = []
        self.scroll_to_bottom()
        cells = self.find_all(self.EMPLOYEE_NAME_CELLS)
        for cell in cells:
            text = cell.text.strip()
            if text:
                names.append(text)
        return names

    def verify_employee_present(self, full_name):
        """Search for a specific employee, confirm it's listed, and print confirmation."""
        self.search_by_name(full_name)
        self.scroll_to_bottom()
        names = self.get_all_employee_names()
        found = any(full_name.lower() in n.lower() for n in names)
        if found:
            print(f"Name Verified: {full_name}")
        else:
            print(f"Name NOT found: {full_name}")
        return found
