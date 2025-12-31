# EM2M Test Automation Framework

A comprehensive Python Behave BDD (Behavior-Driven Development) test automation framework for the EM2M application.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Writing Test Cases](#writing-test-cases)
- [Page Object Model](#page-object-model)
- [Reports](#reports)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Project Structure

```
EM2M_Testcases/
│
├── features/                          # Feature files and test scenarios
│   ├── environment.py                 # Behave hooks (before/after scenarios)
│   ├── login.feature                  # Login feature test scenarios
│   ├── assets.feature                 # Assets management test scenarios
│   │
│   └── steps/                         # Step definitions
│       ├── login_steps.py             # Login step implementations
│       ├── assets_steps.py            # Assets step implementations
│       └── common_steps.py            # Reusable common steps
│
├── pages/                             # Page Object Model (POM) classes
│   ├── base_page.py                   # Base page with common methods
│   ├── login_page.py                  # Login page object
│   └── assets_page.py                 # Assets page object
│
├── utilities/                         # Helper utilities
│   └── helpers.py                     # Common helper functions
│
├── config/                            # Configuration files
│   └── config.py                      # Test configuration settings
│
├── reports/                           # Test execution reports (auto-generated)
│   ├── screenshots/                   # Screenshots on test failure
│   └── junit/                         # JUnit XML reports
│
├── requirements.txt                   # Python dependencies
├── behave.ini                         # Behave configuration
├── .env.example                       # Example environment variables
├── .env                               # Environment variables (create from .env.example)
└── README.md                          # This file
```

## Prerequisites

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **Chrome/Firefox**: Browser for test execution
- **Git**: Version control

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd EM2M_Testcases
```

### 2. Create virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your credentials
# Update BASE_URL, TEST_USERNAME, TEST_PASSWORD, etc.
```

## Configuration

### Environment Variables (.env)

Create a `.env` file in the project root:

```env
# Application URLs
BASE_URL=https://elasticm2m-dev.app.em2m.net
API_BASE_URL=https://elasticm2m-dev.app.em2m.net/api

# Test Credentials
TEST_USERNAME=your_username@em2m.net
TEST_PASSWORD=your_password

# Browser Settings
BROWSER=chrome
HEADLESS=false
WINDOW_SIZE=1920,1080

# Timeout Settings
DEFAULT_TIMEOUT=10
PAGE_LOAD_TIMEOUT=30
```

### Behave Configuration (behave.ini)

The `behave.ini` file contains default Behave settings:
- Output format
- Report paths
- Logging configuration
- Tags configuration

## Running Tests

### Run all tests

```bash
behave
```

### Run specific feature

```bash
behave features/login.feature
behave features/assets.feature
```

### Run tests by tags

```bash
# Run only smoke tests
behave --tags=@smoke

# Run login tests
behave --tags=@login

# Exclude certain tags
behave --tags=-@wip

# Combine tags (AND)
behave --tags=@smoke --tags=@login

# Combine tags (OR)
behave --tags=@smoke,@login
```

### Run specific scenario

```bash
# By line number
behave features/login.feature:10

# By scenario name
behave --name "Successful login"
```

### Headless mode

```bash
# Set in .env file
HEADLESS=true

# Or run with environment variable
HEADLESS=true behave
```

### Generate reports

```bash
# JUnit XML report (configured in behave.ini)
behave --junit

# Allure report
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results
```

## Writing Test Cases

### 1. Create a Feature File

Feature files are written in Gherkin syntax and stored in the `features/` directory.

**Example: `features/user_profile.feature`**

```gherkin
Feature: User Profile Management
  As a user of the EM2M application
  I want to manage my profile
  So that I can keep my information up to date

  Background:
    Given the user is logged in
    And the user is on the profile page

  @smoke @profile
  Scenario: View user profile
    When the user navigates to the profile page
    Then the user should see their profile information
    And the profile should display name and email

  @profile @edit
  Scenario: Edit user profile
    When the user clicks the "Edit Profile" button
    And the user updates the name to "New Name"
    And the user clicks the "Save" button
    Then the profile should be updated successfully
    And the user should see a success message

  @profile
  Scenario Outline: Update profile with different values
    When the user updates "<field>" to "<value>"
    And the user saves the changes
    Then the "<field>" should be updated to "<value>"

    Examples:
      | field | value           |
      | name  | John Doe        |
      | email | john@example.com|
      | phone | 555-1234        |
```

### 2. Create Step Definitions

Step definitions implement the steps from your feature files. Create them in `features/steps/`.

**Example: `features/steps/profile_steps.py`**

```python
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.profile_page import ProfilePage


@given('the user is on the profile page')
def step_navigate_to_profile(context):
    """Navigate to the profile page."""
    context.profile_page = ProfilePage(context.driver)
    context.profile_page.navigate_to_profile()


@when('the user navigates to the profile page')
def step_go_to_profile(context):
    """Navigate to profile page."""
    context.profile_page.navigate_to_profile()


@when('the user updates the name to "{new_name}"')
def step_update_name(context, new_name):
    """Update the user name."""
    context.profile_page.update_name(new_name)
    context.updated_name = new_name


@then('the user should see their profile information')
def step_verify_profile_info(context):
    """Verify profile information is displayed."""
    assert context.profile_page.is_profile_displayed(), \
        "Profile information is not displayed"


@then('the profile should display name and email')
def step_verify_name_email(context):
    """Verify name and email are displayed."""
    assert context.profile_page.is_name_displayed(), "Name not displayed"
    assert context.profile_page.is_email_displayed(), "Email not displayed"
```

### 3. Create Page Objects

Page Objects encapsulate page interactions. Create them in the `pages/` directory.

**Example: `pages/profile_page.py`**

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    """Profile page object."""

    # Locators
    PROFILE_NAME = (By.ID, "profile-name")
    PROFILE_EMAIL = (By.ID, "profile-email")
    EDIT_BUTTON = (By.CSS_SELECTOR, "button.edit-profile")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button.save-profile")
    NAME_INPUT = (By.ID, "input-name")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")

    def __init__(self, driver):
        """Initialize the profile page."""
        super().__init__(driver)
        self.base_url = "https://elasticm2m-dev.app.em2m.net"

    def navigate_to_profile(self):
        """Navigate to the profile page."""
        profile_url = f"{self.base_url}/profile"
        self.navigate_to(profile_url)

    def is_profile_displayed(self):
        """Check if profile is displayed."""
        return self.is_element_visible(*self.PROFILE_NAME)

    def is_name_displayed(self):
        """Check if name is displayed."""
        return self.is_element_visible(*self.PROFILE_NAME)

    def is_email_displayed(self):
        """Check if email is displayed."""
        return self.is_element_visible(*self.PROFILE_EMAIL)

    def click_edit_button(self):
        """Click the edit button."""
        self.click(*self.EDIT_BUTTON)

    def update_name(self, new_name):
        """Update the name field."""
        self.enter_text(*self.NAME_INPUT, new_name)

    def click_save_button(self):
        """Click the save button."""
        self.click(*self.SAVE_BUTTON)

    def get_success_message(self):
        """Get the success message."""
        return self.get_text(*self.SUCCESS_MESSAGE)
```

### 4. Update Locators

**Important**: Update the locators in page objects to match your actual application's HTML structure.

To find correct locators:
1. Open your application in Chrome
2. Right-click on an element → Inspect
3. Use Chrome DevTools to identify:
   - ID: `id="login-button"` → `By.ID, "login-button"`
   - Class: `class="btn-primary"` → `By.CSS_SELECTOR, ".btn-primary"`
   - XPath: Right-click element → Copy → Copy XPath
   - Name: `name="username"` → `By.NAME, "username"`

## Page Object Model

### Base Page

The `BasePage` class provides common methods used across all pages:

- `find_element()` - Find single element with wait
- `find_elements()` - Find multiple elements
- `click()` - Click with wait
- `enter_text()` - Enter text in input field
- `get_text()` - Get element text
- `is_element_visible()` - Check visibility
- `wait_for_url_contains()` - Wait for URL
- `scroll_to_element()` - Scroll to element

### Creating New Page Objects

1. Inherit from `BasePage`
2. Define locators as class variables
3. Implement page-specific methods
4. Keep methods atomic and reusable

**Example Template:**

```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NewPage(BasePage):
    """New page object."""

    # Locators
    ELEMENT_1 = (By.ID, "element-id")
    ELEMENT_2 = (By.CSS_SELECTOR, ".element-class")

    def __init__(self, driver):
        """Initialize the page."""
        super().__init__(driver)

    def perform_action(self):
        """Perform an action on the page."""
        self.click(*self.ELEMENT_1)

    def verify_element(self):
        """Verify an element is visible."""
        return self.is_element_visible(*self.ELEMENT_2)
```

## Reports

### JUnit Reports

JUnit XML reports are generated automatically in `reports/junit/` directory.

```bash
behave --junit
```

### Allure Reports

Generate beautiful HTML reports with Allure:

```bash
# Run tests with Allure formatter
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# View the report
allure serve allure-results
```

### Screenshots

Screenshots are automatically captured on test failure and saved in `reports/screenshots/`.

## Best Practices

### 1. Feature File Guidelines

- Use descriptive feature and scenario names
- Follow Gherkin syntax strictly
- Use tags for organization (@smoke, @regression, @wip)
- Keep scenarios independent
- Use Background for common preconditions
- Use Scenario Outline for data-driven tests

### 2. Step Definition Guidelines

- Keep steps simple and atomic
- Reuse steps across features
- Use clear assertion messages
- Implement proper waits (avoid `time.sleep()`)
- Handle exceptions gracefully

### 3. Page Object Guidelines

- One page object per page
- Use descriptive locator names
- Prefer CSS selectors over XPath when possible
- Keep methods focused and single-purpose
- Return page objects for method chaining

### 4. Naming Conventions

- Feature files: `lowercase_with_underscores.feature`
- Step files: `descriptive_steps.py`
- Page objects: `PascalCase` for classes
- Methods: `snake_case`
- Locators: `UPPER_CASE_WITH_UNDERSCORES`

### 5. Test Data Management

- Store test data in separate files
- Use environment variables for credentials
- Generate unique data for each test run
- Clean up test data after execution

## Troubleshooting

### Common Issues

**Issue**: `WebDriverException: Chrome driver not found`
```bash
# Solution: Reinstall webdriver-manager
pip install --upgrade webdriver-manager
```

**Issue**: `ElementNotInteractableException`
```python
# Solution: Add explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "element-id"))
)
element.click()
```

**Issue**: Tests failing due to incorrect locators
```
# Solution: Update locators in page objects to match your application
# Use Chrome DevTools to inspect elements and get correct selectors
```

**Issue**: `ModuleNotFoundError`
```bash
# Solution: Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Debug Mode

Run Behave with verbose output:

```bash
behave --no-capture --no-capture-stderr -v
```

### Browser DevTools

Keep browser open on failure:

```python
# In features/environment.py, comment out driver.quit()
def after_scenario(context, scenario):
    if scenario.status == 'failed':
        # Don't quit browser on failure for debugging
        pass
    else:
        context.driver.quit()
```

## Contributing

1. Create a feature branch
2. Write tests following the guidelines
3. Ensure all tests pass
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created and configured
- [ ] Chrome browser installed
- [ ] Update page object locators to match your application
- [ ] Run sample test: `behave features/login.feature`
- [ ] Review test reports in `reports/` directory

## Support

For issues and questions:
- Create an issue in the repository
- Contact the QA team
- Check the Behave documentation: https://behave.readthedocs.io/

---

**Happy Testing!** 🚀
