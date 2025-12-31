# Quick Setup Guide

Follow these steps to set up the EM2M test automation framework.

## Prerequisites

- Python 3.8 or higher installed
- Chrome browser installed
- Git installed

## Setup Steps

### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env
```

Then edit `.env` and update:
- `BASE_URL` - Your application URL
- `TEST_USERNAME` - Your test username
- `TEST_PASSWORD` - Your test password

### 4. Update Page Locators

**IMPORTANT**: Before running tests, update the locators in the page object files to match your actual application:

1. Open your application in Chrome
2. Right-click elements and inspect them
3. Update the locators in:
   - `pages/login_page.py`
   - `pages/assets_page.py`

Example:
```python
# If your username field has id="email"
USERNAME_INPUT = (By.ID, "email")  # Update from "username" to "email"
```

### 5. Run Your First Test

**Windows:**
```bash
run_tests.bat login
```

**macOS/Linux:**
```bash
./run_tests.sh login
```

Or use behave directly:
```bash
behave features/login.feature
```

## Common Commands

```bash
# Run all tests
behave

# Run smoke tests only
behave --tags=@smoke

# Run with custom script (Windows)
run_tests.bat smoke
run_tests.bat login
run_tests.bat assets

# Run with custom script (macOS/Linux)
./run_tests.sh smoke
./run_tests.sh login
./run_tests.sh assets

# Generate Allure report
./run_tests.sh report  # or run_tests.bat report
```

## Next Steps

1. Inspect your application to get the correct element locators
2. Update all page objects with correct locators
3. Customize feature files for your specific test cases
4. Add more page objects as needed
5. Create additional feature files for other functionalities

## Need Help?

Check the main [README.md](README.md) for detailed documentation.
