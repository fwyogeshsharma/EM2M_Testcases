# EM2M Test Automation - Quick Reference Guide

## 📁 Project Structure Overview

```
EM2M_Testcases/
├── features/               # Test scenarios (Gherkin)
│   ├── login.feature      ✅ Login tests (4 scenarios)
│   ├── search.feature     ✅ Search tests (3 scenarios)
│   ├── assets.feature     ⚠️  Asset tests (5 scenarios - skeleton)
│   ├── environment.py     # Behave hooks
│   └── steps/             # Step implementations
│       ├── login_steps.py
│       ├── search_steps.py
│       ├── assets_steps.py
│       └── common_steps.py
│
├── pages/                 # Page Object Model
│   ├── base_page.py      # Base class
│   ├── login_page.py     ✅ Working
│   ├── search_page.py    ✅ Working
│   └── assets_page.py    ⚠️  Needs locator updates
│
├── config/                # Configuration
│   └── config.py         # Settings & credentials
│
├── utilities/             # Helper functions
│   └── helpers.py
│
└── reports/               # Test results
    └── screenshots/       # Failure screenshots
```

## 🚀 Quick Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your credentials

# Verify structure
python verify_structure.py
```

### Run Tests
```bash
# All tests
behave

# Specific feature
behave features/login.feature
behave features/search.feature

# By tags
behave --tags=@smoke        # Smoke tests only
behave --tags=@login        # Login tests
behave --tags=@search       # Search tests

# Specific scenario (by line number)
behave features/search.feature:10

# With output
behave --no-capture         # Show print statements
behave -v                   # Verbose mode
```

### Cleanup
```bash
# Windows
cleanup.bat

# Linux/Mac
./cleanup.sh
```

## 📊 Test Status

| Feature | Scenarios | Status | Coverage |
|---------|-----------|--------|----------|
| Login | 4 | ✅ PASS | 100% |
| Search | 3 | ✅ PASS | 100% |
| Assets | 5 | ⚠️ SKELETON | 0% |
| **Total** | **12** | **58%** | **7/12 passing** |

## 🏷️ Tag Reference

```bash
@smoke      # Critical smoke tests
@login      # All login tests
@search     # All search tests
@assets     # All asset tests
@negative   # Negative/error cases
@create     # Create operations
@edit       # Edit operations
@delete     # Delete operations
```

## 🔑 Key Locators

### Login Page
```python
USERNAME = (By.NAME, "username")
PASSWORD = (By.NAME, "password")
LOGIN_BTN = (By.CSS_SELECTOR, "button.form-login-button")
```

### Search Page
```python
# Search button (found dynamically by text "search")
# Search input (appears AFTER clicking search button)
DROPDOWN = (By.CSS_SELECTOR, "mat-option[role='option']")
```

## 📝 File Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `{name}.feature` | `login.feature` |
| Steps | `{name}_steps.py` | `login_steps.py` |
| Page Object | `{name}_page.py` | `login_page.py` |

## 🔍 Common Tasks

### Add New Test Feature
1. Create `features/new_feature.feature`
2. Create `features/steps/new_feature_steps.py`
3. Create `pages/new_feature_page.py`
4. Update documentation

### Debug Test Failure
1. Check screenshot in `reports/screenshots/`
2. Run with `--no-capture` to see prints
3. Verify locators in page object
4. Check waits and timeouts

### Update Locators
1. Open page object file (e.g., `pages/login_page.py`)
2. Update locator at top of class
3. Re-run tests to verify

## 📞 Help & Documentation

| Document | Purpose |
|----------|---------|
| `README.md` | Project overview |
| `SETUP_GUIDE.md` | Installation instructions |
| `PROJECT_STRUCTURE.md` | Detailed file structure |
| `TEST_SUMMARY.md` | Complete test inventory |
| `QUICK_REFERENCE.md` | This guide |

## ⚡ Most Used Commands

```bash
# Quick smoke test
behave --tags=@smoke

# Run login tests only
behave features/login.feature

# Run search test for ASEED
behave features/search.feature:10

# Debug with prints
behave --no-capture

# Verify project structure
python verify_structure.py
```

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Element not found | Check locators in page objects |
| Timeout | Increase timeout in `config.py` |
| Login failed | Verify credentials in `.env` |
| Import error | Run from project root |
| Search dropdown missing | Ensure typing in correct input |

## 📈 Next Steps

- [ ] Update Assets page locators
- [ ] Implement Assets tests
- [ ] Add more edge cases
- [ ] Set up CI/CD
- [ ] Generate HTML reports

---

**Last Updated**: December 31, 2024
**Framework**: Behave + Selenium + Python
