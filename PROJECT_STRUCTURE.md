# EM2M Test Automation - Project Structure

## Directory Structure

```
EM2M_Testcases/
│
├── config/                          # Configuration files
│   ├── __init__.py
│   └── config.py                    # Test configuration and environment variables
│
├── features/                        # BDD feature files (Gherkin)
│   ├── environment.py               # Behave hooks (before/after scenarios)
│   ├── login.feature                # Login test scenarios
│   ├── search.feature               # Search functionality tests
│   ├── assets.feature               # Asset management tests
│   │
│   └── steps/                       # Step definitions for features
│       ├── __init__.py
│       ├── login_steps.py           # Login step implementations
│       ├── search_steps.py          # Search step implementations
│       ├── assets_steps.py          # Assets step implementations
│       └── common_steps.py          # Reusable common step definitions
│
├── pages/                           # Page Object Model (POM)
│   ├── __init__.py
│   ├── base_page.py                 # Base page class with common methods
│   ├── login_page.py                # Login page object
│   ├── search_page.py               # Search page object
│   └── assets_page.py               # Assets page object
│
├── utilities/                       # Helper functions and utilities
│   ├── __init__.py
│   └── helpers.py                   # Common helper functions
│
├── reports/                         # Test execution reports
│   └── screenshots/                 # Screenshots on test failures
│
├── .env                             # Environment variables (credentials, URLs)
├── .env.example                     # Example environment variables file
├── .gitignore                       # Git ignore patterns
├── behave.ini                       # Behave configuration
├── requirements.txt                 # Python dependencies
├── run_tests.bat                    # Windows test execution script
├── run_tests.sh                     # Linux/Mac test execution script
├── README.md                        # Project documentation
└── SETUP_GUIDE.md                   # Setup instructions
```

## File Naming Conventions

### Feature Files
- **Location**: `features/`
- **Pattern**: `{feature_name}.feature`
- **Examples**:
  - `login.feature`
  - `search.feature`
  - `assets.feature`

### Step Definition Files
- **Location**: `features/steps/`
- **Pattern**: `{feature_name}_steps.py`
- **Examples**:
  - `login_steps.py`
  - `search_steps.py`
  - `assets_steps.py`
  - `common_steps.py` (for shared steps)

### Page Object Files
- **Location**: `pages/`
- **Pattern**: `{page_name}_page.py`
- **Examples**:
  - `login_page.py`
  - `search_page.py`
  - `assets_page.py`
  - `base_page.py` (parent class for all pages)

## File Relationships

```
login.feature ──► login_steps.py ──► login_page.py
search.feature ──► search_steps.py ──► search_page.py
assets.feature ──► assets_steps.py ──► assets_page.py
                      │
                      ▼
                common_steps.py (shared steps)
                      │
                      ▼
All page objects inherit from ──► base_page.py
```

## Test Execution Flow

1. **Behave reads** `features/*.feature` files
2. **Matches steps** with definitions in `features/steps/*_steps.py`
3. **Step definitions** interact with page objects in `pages/*_page.py`
4. **Page objects** perform actions on web elements
5. **Results** are stored in `reports/` directory

## Current Test Coverage

### 1. Login Feature (`login.feature`)
- ✅ Successful login with valid credentials
- ✅ Login with invalid credentials
- ✅ Login with empty credentials
- ✅ Login with different user roles

**Files**:
- Feature: `features/login.feature`
- Steps: `features/steps/login_steps.py`
- Page Object: `pages/login_page.py`

### 2. Search Feature (`search.feature`)
- ✅ Search for ASEED and select exact match
- ✅ Search for item and verify results
- ✅ Search for different items (parameterized)

**Files**:
- Feature: `features/search.feature`
- Steps: `features/steps/search_steps.py`
- Page Object: `pages/search_page.py`

### 3. Assets Management Feature (`assets.feature`)
- ⚠️ View asset list
- ⚠️ Create a new asset
- ⚠️ Edit an existing asset
- ⚠️ Delete an asset
- ⚠️ Search for assets

**Files**:
- Feature: `features/assets.feature`
- Steps: `features/steps/assets_steps.py`
- Page Object: `pages/assets_page.py`

**Note**: ⚠️ = Skeleton implemented, needs locator updates based on actual application

## Configuration Files

### 1. `config/config.py`
Centralized configuration for:
- Application URLs (BASE_URL, LOGIN_URL, etc.)
- Test credentials (usernames, passwords)
- Browser settings (browser type, headless mode)
- Timeout settings
- Report directories

### 2. `.env`
Contains sensitive data (not committed to Git):
```env
BASE_URL=https://elasticm2m-dev.app.em2m.net
TEST_USERNAME=your_username
TEST_PASSWORD=your_password
```

### 3. `behave.ini`
Behave framework configuration:
- Default tags to run
- Output formats
- Logging settings

## Running Tests

### Run All Tests
```bash
# Windows
run_tests.bat

# Linux/Mac
./run_tests.sh
```

### Run Specific Feature
```bash
behave features/login.feature
behave features/search.feature
behave features/assets.feature
```

### Run Specific Scenario
```bash
behave features/search.feature:10
```

### Run by Tags
```bash
behave --tags=@smoke
behave --tags=@login
behave --tags=@search
behave --tags="@smoke and @search"
```

## Best Practices

### 1. Feature Files
- Write in natural language (Gherkin)
- Focus on business behavior, not implementation
- Use descriptive scenario names
- Group related scenarios in one feature file

### 2. Step Definitions
- Keep steps simple and reusable
- Avoid hard-coded values, use parameters
- Put common steps in `common_steps.py`
- One step definition file per feature

### 3. Page Objects
- One page object per application page
- All locators defined at the top of the class
- Methods should represent user actions
- Inherit from `base_page.py` for common functionality
- Never put assertions in page objects

### 4. Naming Conventions
- **Files**: Use lowercase with underscores (`login_page.py`)
- **Classes**: Use PascalCase (`LoginPage`)
- **Methods**: Use snake_case (`click_login_button`)
- **Variables**: Use snake_case (`search_term`)

## Adding New Tests

### To add a new feature:

1. **Create feature file**: `features/new_feature.feature`
2. **Create step definitions**: `features/steps/new_feature_steps.py`
3. **Create page object**: `pages/new_feature_page.py`
4. **Update this documentation**

### Template:

**Feature file** (`features/new_feature.feature`):
```gherkin
Feature: Feature Name
  As a user
  I want to do something
  So that I can achieve a goal

  @tag
  Scenario: Scenario name
    Given initial condition
    When user action
    Then expected result
```

**Step definitions** (`features/steps/new_feature_steps.py`):
```python
from behave import given, when, then
from pages.new_feature_page import NewFeaturePage

@given('initial condition')
def step_impl(context):
    context.page = NewFeaturePage(context.driver)
    # implementation
```

**Page object** (`pages/new_feature_page.py`):
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NewFeaturePage(BasePage):
    # Locators
    ELEMENT = (By.CSS_SELECTOR, ".class")

    def __init__(self, driver):
        super().__init__(driver)

    def perform_action(self):
        # implementation
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you're running from project root
2. **Element not found**: Check locators in page objects
3. **Timeout errors**: Increase waits in `config.py`
4. **Login failures**: Check credentials in `.env`

### Debug Tips

- Use `--no-capture` flag to see print statements
- Check screenshots in `reports/screenshots/` on failures
- Run with `-v` for verbose output
- Use `@wip` tag for work-in-progress tests

## Maintenance

### Regular Tasks
- [ ] Update locators when UI changes
- [ ] Add new test scenarios as features are developed
- [ ] Review and refactor duplicate code
- [ ] Update dependencies in `requirements.txt`
- [ ] Clean up old screenshots from `reports/`

### Code Quality
- Follow PEP 8 style guidelines
- Keep methods small and focused
- Write descriptive variable names
- Comment complex logic
- Remove unused imports and code

---

**Last Updated**: December 31, 2024
**Project**: EM2M Test Automation
**Framework**: Behave + Selenium + Python
