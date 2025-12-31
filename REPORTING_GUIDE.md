# EM2M Test Automation - Reporting Guide

## 📊 Overview

This project uses **Allure Reports** - a flexible, beautiful reporting framework that provides:
- ✅ **Beautiful UI** with charts and graphs
- ✅ **Pass/Fail percentages** with visual metrics
- ✅ **Detailed test results** with screenshots
- ✅ **Test history** and trends
- ✅ **Categorization** by features and tags
- ✅ **Execution timeline** and duration

---

## 🚀 Quick Start - Generate Report

### Windows
```bash
# Run tests and generate report
generate_report.bat

# Or run specific tests
run_tests_with_report.bat

# View existing report
view_report.bat
```

### Linux/Mac
```bash
# Run tests and generate report
./generate_report.sh

# View existing report
./view_report.sh
```

---

## 📦 Prerequisites

### Install Allure Command Line Tool

#### Windows (using Scoop)
```bash
# Install Scoop (if not installed)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Install Allure
scoop install allure
```

#### Windows (Manual Installation)
1. Download from: https://github.com/allure-framework/allure2/releases
2. Extract to `C:\allure`
3. Add `C:\allure\bin` to PATH

#### Mac
```bash
brew install allure
```

#### Linux
```bash
# Download and extract
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz
sudo mv allure-2.24.0 /opt/allure

# Add to PATH
echo 'export PATH="$PATH:/opt/allure/bin"' >> ~/.bashrc
source ~/.bashrc
```

---

## 📝 Generating Reports

### Method 1: Using Scripts (Recommended)

**Generate Full Report:**
```bash
# Windows
generate_report.bat

# Linux/Mac
./generate_report.sh
```

**Run Tests with Report:**
```bash
# Windows
run_tests_with_report.bat

# Linux/Mac
./run_tests_with_report.sh
```

### Method 2: Manual Commands

**Step 1: Run Tests with Allure Formatter**
```bash
# Run all tests
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# Run smoke tests only
behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=@smoke

# Run specific feature
behave features/login.feature -f allure_behave.formatter:AllureFormatter -o allure-results
```

**Step 2: Generate Report**
```bash
allure generate allure-results --clean -o allure-report
```

**Step 3: Open Report**
```bash
allure open allure-report
```

### Method 3: Run with Multiple Formatters

```bash
# Pretty console output + Allure report
behave -f pretty -f allure_behave.formatter:AllureFormatter -o allure-results
```

---

## 🎨 Report Features

### 1. **Overview Dashboard**
- Total test count
- Pass/Fail percentage with pie charts
- Test duration
- Execution timeline

### 2. **Suites View**
- Tests grouped by features
- Individual scenario results
- Duration for each test

### 3. **Graphs**
- Status breakdown (Passed/Failed/Skipped)
- Severity distribution
- Duration trends

### 4. **Timeline**
- Visual timeline of test execution
- Parallel execution visualization

### 5. **Behaviors**
- Tests grouped by features/stories
- Epic-Feature-Story hierarchy

### 6. **Packages**
- Tests organized by package structure

### 7. **Categories**
- Test failures categorized:
  - Product defects
  - Test defects
  - Environment issues

---

## 📸 Screenshots in Reports

Screenshots are **automatically attached** to failed tests:

1. Test fails → Screenshot captured
2. Screenshot saved to `reports/screenshots/`
3. Screenshot attached to Allure report
4. Visible in the failed test details

**View in Report:**
- Open failed test
- Scroll down to "Attachments"
- Click to view full screenshot

---

## 📊 Understanding Report Metrics

### Pass Rate Calculation
```
Pass Rate = (Passed Tests / Total Tests) × 100%
```

### Example Report Output:
```
Total Tests: 7
Passed: 7
Failed: 0
Skipped: 0

Pass Rate: 100%
```

### Status Indicators:
- 🟢 **Passed** - Test executed successfully
- 🔴 **Failed** - Test failed (with screenshot)
- ⚪ **Skipped** - Test was skipped
- 🟡 **Broken** - Test setup/teardown issues

---

## 🏷️ Tagging for Better Reports

Allure supports categorization using Behave tags:

```gherkin
@smoke @severity:critical
Scenario: Critical login test
  Given user is on login page
  When user enters credentials
  Then user should be logged in
```

**Severity Levels:**
- `@severity:blocker`
- `@severity:critical`
- `@severity:normal`
- `@severity:minor`
- `@severity:trivial`

**Epic/Feature/Story:**
```gherkin
@epic:Authentication
@feature:Login
@story:UserLogin
Scenario: User login with valid credentials
```

---

## 📁 Report Directory Structure

```
allure-results/          # Test execution data (JSON)
├── *-result.json        # Individual test results
├── *-container.json     # Test grouping data
└── *-attachment.png     # Screenshots

allure-report/           # Generated HTML report
├── index.html           # Main report page
├── data/                # Report data
├── styles/              # CSS files
└── history/             # Historical data
```

---

## 🔄 Report History & Trends

Allure can show test execution **trends over time**:

**Enable History:**
```bash
# After first run
allure generate allure-results --clean -o allure-report

# For subsequent runs (keeps history)
cp -r allure-report/history allure-results/history
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results --clean -o allure-report
```

**View Trends:**
- Open report
- Go to "Graphs" tab
- See historical trend lines

---

## 🎯 Customizing Reports

### Add Environment Information

Create `allure-results/environment.properties`:
```properties
Browser=Chrome
Browser.Version=120.0
Base.URL=https://elasticm2m-dev.app.em2m.net
Environment=Development
OS=Windows 11
Python.Version=3.11
```

**Auto-generate (add to environment.py):**
```python
import json

def after_all(context):
    # Create environment info
    env_info = {
        "Browser": "Chrome",
        "Base URL": context.base_url,
        "Python Version": "3.11"
    }

    with open('allure-results/environment.properties', 'w') as f:
        for key, value in env_info.items():
            f.write(f"{key}={value}\n")
```

### Add Categories

Create `allure-results/categories.json`:
```json
[
  {
    "name": "Product Defects",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*AssertionError.*"
  },
  {
    "name": "Element Not Found",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*NoSuchElementException.*"
  },
  {
    "name": "Timeout Issues",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*TimeoutException.*"
  }
]
```

---

## 📤 Sharing Reports

### Option 1: Open Locally
```bash
allure open allure-report
```

### Option 2: Serve on Network
```bash
# Start server on port 8080
allure serve allure-results -h 0.0.0.0 -p 8080
```

### Option 3: Static HTML
- Copy `allure-report/` folder
- Host on web server (Apache, Nginx, etc.)
- Or use GitHub Pages

### Option 4: CI/CD Integration
- Jenkins: Allure Jenkins Plugin
- GitLab: Allure GitLab Plugin
- GitHub Actions: Publish Allure Report action

---

## 🐛 Troubleshooting

### Issue: "Allure command not found"
**Solution:**
- Verify installation: `allure --version`
- Check PATH includes Allure bin directory
- Reinstall Allure

### Issue: "No test results found"
**Solution:**
- Ensure you ran tests with Allure formatter
- Check `allure-results/` directory exists and has JSON files
- Verify behave command included `-o allure-results`

### Issue: "Report shows 0 tests"
**Solution:**
- Delete `allure-results/` and run tests again
- Ensure `-f allure_behave.formatter:AllureFormatter` is used
- Check behave runs successfully

### Issue: Screenshots not appearing
**Solution:**
- Check `reports/screenshots/` has PNG files
- Verify `environment.py` has Allure attachment code
- Ensure tests are actually failing (screenshots only on failures)

---

## 📊 Sample Report Commands

```bash
# Run all tests and view report
behave -f allure_behave.formatter:AllureFormatter -o allure-results && allure serve allure-results

# Run smoke tests only
behave --tags=@smoke -f allure_behave.formatter:AllureFormatter -o allure-results

# Run and open report in browser
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report

# Generate report without opening
allure generate allure-results --clean -o allure-report
```

---

## 📈 Best Practices

1. **Tag Appropriately**
   - Use `@severity` tags for prioritization
   - Use `@epic/@feature/@story` for organization

2. **Clean Results Between Runs**
   - Use `--clean` flag when generating
   - Or delete `allure-results/` before tests

3. **Keep History**
   - Save history folder for trends
   - Useful for tracking test stability

4. **Add Descriptions**
   - Use docstrings in step definitions
   - Adds context in reports

5. **Review Reports Regularly**
   - Check failure categories
   - Identify flaky tests
   - Track improvement trends

---

## 🔗 Additional Resources

- **Allure Documentation**: https://docs.qameta.io/allure/
- **Allure Behave**: https://github.com/allure-framework/allure-python
- **Allure Examples**: https://demo.qameta.io/allure/

---

## 📞 Quick Reference

| Task | Command |
|------|---------|
| Run with report | `behave -f allure_behave.formatter:AllureFormatter -o allure-results` |
| Generate report | `allure generate allure-results --clean -o allure-report` |
| Open report | `allure open allure-report` |
| Serve report | `allure serve allure-results` |
| Check version | `allure --version` |

---

**Last Updated**: December 31, 2024
**Report Framework**: Allure 2.x
**Integration**: Behave + Allure
