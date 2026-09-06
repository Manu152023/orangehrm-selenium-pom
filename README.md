# OrangeHRM – Selenium POM Automation Suite

Automates login and employee-management workflows for the OrangeHRM demo site
(`https://opensource-demo.orangehrmlive.com/web/index.php/auth/login`) using
Python, Selenium WebDriver, and the Page Object Model (POM) design pattern.

## Project Structure
```
orangehrm_pom/
├── pages/
│   ├── base_page.py           # Shared wait/click/type helpers
│   ├── login_page.py          # Login screen locators + actions
│   ├── dashboard_page.py      # Nav bar: PIM link, user dropdown, logout
│   ├── pim_page.py            # PIM landing page: Add Employee / Employee List
│   ├── add_employee_page.py   # Add Employee form
│   └── employee_list_page.py  # Employee List: search, scroll, verify names
├── tests/
│   ├── test_login.py              # Pytest suite for login scenarios
│   └── test_employee_workflow.py  # Full end-to-end workflow script
├── requirements.txt
└── README.md
```

## Setup
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Google Chrome must be installed locally. `webdriver-manager` automatically
downloads the matching ChromeDriver version.

## Running the tests

**1. Full workflow (login → PIM → add employees → verify → logout):**
```bash
python3 -m tests.test_employee_workflow
```
Console output will include lines like:
```
Login successful.
Navigated to PIM module.
Added employee: John Carter
...
Name Verified: John Carter
Name Verified: Emma Watson
...
Logout successful. Workflow complete.
```

**2. Login-only pytest suite:**
```bash
pytest tests/test_login.py -v
```

## Notes
- Credentials used: `Admin` / `admin123` (the demo site's default credentials,
  as shown on the login page itself).
- Locators are based on the current OrangeHRM demo build; if the demo site's
  UI changes, update the locators in the relevant `pages/*.py` file only —
  this is the core benefit of the Page Object Model.
- To run headless (e.g., in CI), uncomment the
  `options.add_argument("--headless=new")` line in each test file.
