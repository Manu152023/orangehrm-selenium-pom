"""
End-to-end automated workflow test for OrangeHRM using Selenium + Page Object Model.

Workflow:
1. Login
2. Hover over PIM in the nav bar and click it
3. Add 3-4 new employees via 'Add Employee'
4. Navigate to Employee List, scroll, and verify each added employee's name
   -> prints "Name Verified" for each match found
5. Logout

Run with: python -m tests.test_employee_workflow   (from the orangehrm_pom/ root)
Requires: selenium, webdriver-manager
    pip install selenium webdriver-manager
"""
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage

# --- Test data ---
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"

NEW_EMPLOYEES = [
    ("John", "Carter"),
    ("Emma", "Watson"),
    ("Liam", "Brown"),
    ("Olivia", "Davis"),
]


def build_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # uncomment to run headless
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def run_workflow():
    driver = build_driver()
    try:
        # 1. Login
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_loaded(), "Login failed - Dashboard not loaded"
        print("Login successful.")

        # 2. Hover over PIM and click
        dashboard_page.go_to_pim()
        pim_page = PimPage(driver)
        print("Navigated to PIM module.")

        # 3. Add employees
        for first, last in NEW_EMPLOYEES:
            pim_page.click_add_employee()
            add_employee_page = AddEmployeePage(driver)
            add_employee_page.add_employee(first, last)
            print(f"Added employee: {first} {last}")
            # go back to PIM page to add the next employee
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule")
            time.sleep(1)

        # 4. Verify employees in Employee List
        pim_page.go_to_employee_list()
        employee_list_page = EmployeeListPage(driver)

        all_verified = True
        for first, last in NEW_EMPLOYEES:
            full_name = f"{first} {last}"
            found = employee_list_page.verify_employee_present(full_name)
            all_verified = all_verified and found

        if all_verified:
            print("All employees verified successfully in Employee List.")
        else:
            print("Some employees could not be verified. Check logs above.")

        # 5. Logout
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        dashboard_page.logout()
        login_page_check = LoginPage(driver)
        assert login_page_check.is_visible(login_page_check.USERNAME_INPUT), \
            "Logout failed - login page not shown"
        print("Logout successful. Workflow complete.")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    run_workflow()
