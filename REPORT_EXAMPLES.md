# Allure Report - Visual Examples & Features

## 📊 What You'll See in Reports

This document shows what to expect in your Allure reports with examples.

---

## 🏠 Overview Dashboard

When you open the report, you'll see:

```
╔════════════════════════════════════════════════════════╗
║              ALLURE REPORT - OVERVIEW                  ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  Total Tests: 7                    Duration: 3m 45s   ║
║  Passed: 7      Failed: 0                             ║
║                                                        ║
║  ████████████████████████  100%                       ║
║  🟢 Passed    🔴 Failed    ⚪ Skipped                 ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

**Key Metrics Displayed:**
- ✅ Total number of tests
- ✅ Pass/Fail/Skip counts
- ✅ Success percentage
- ✅ Total execution time
- ✅ Pass rate trend (if history enabled)

---

## 📈 Charts & Graphs

### 1. Status Chart (Pie Chart)
```
         Test Results
    ┌─────────────────┐
    │    🟢 100%     │
    │                 │
    │   7 Passed      │
    │   0 Failed      │
    │   0 Skipped     │
    └─────────────────┘
```

### 2. Severity Chart
```
    Severity Distribution

    Critical  ████████ 40%
    Normal    ████████ 40%
    Minor     ████░░░░ 20%
```

### 3. Duration Chart
```
    Test Duration (seconds)

    Login Tests     ████░░░░░░ 25s
    Search Tests    ██████░░░░ 28s
    Asset Tests     ████░░░░░░ 22s
```

---

## 🗂️ Suites View

```
📁 features/
  │
  ├─ 📄 login.feature
  │   ├─ ✅ Successful login with valid credentials (5.2s)
  │   ├─ ✅ Login with invalid credentials (3.1s)
  │   ├─ ✅ Login with empty credentials (2.8s)
  │   └─ ✅ Login with different user roles (6.5s)
  │
  ├─ 📄 search.feature
  │   ├─ ✅ Search for ASEED and select exact match (28.7s)
  │   ├─ ✅ Search for item and verify results (15.2s)
  │   └─ ✅ Search for different items (12.4s)
  │
  └─ 📄 assets.feature
      └─ ⚪ (5 scenarios - not yet run)
```

---

## 🔍 Individual Test Details

When you click on a test, you see:

```
╔══════════════════════════════════════════════════════╗
║  Search for ASEED and select exact match             ║
╠══════════════════════════════════════════════════════╣
║  Status: ✅ PASSED                                   ║
║  Duration: 28.7 seconds                              ║
║  Tags: @smoke, @search                               ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Test Steps:                                         ║
║  ✅ Given the user is logged in with valid creds    ║
║  ✅ When the user clicks the search button          ║
║  ✅ And the user enters "ASEED" in search           ║
║  ✅ And the user waits for the dropdown             ║
║  ✅ Then the user should see "ASEED" in dropdown    ║
║  ✅ When the user clicks on exact match "ASEED"     ║
║  ✅ Then user should be on ASEED details page       ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  Console Output:                                     ║
║  > Found search button with text: 'search'          ║
║  > Clicked search button                            ║
║  > Visible inputs BEFORE: 1                         ║
║  > Visible inputs AFTER: 2                          ║
║  > Found NEW search input                           ║
║  > Typed 'ASEED' successfully                       ║
║  > Dropdown with mat-option elements found          ║
║  > Found 1 visible dropdown options                 ║
║  > Found exact match: 'ASEED', clicking...          ║
╚══════════════════════════════════════════════════════╝
```

---

## 📸 Failed Test with Screenshot

For failed tests, you'll see:

```
╔══════════════════════════════════════════════════════╗
║  Login with invalid credentials                      ║
╠══════════════════════════════════════════════════════╣
║  Status: 🔴 FAILED                                   ║
║  Duration: 5.3 seconds                               ║
║  Tags: @login, @negative                             ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Error Message:                                      ║
║  AssertionError: Expected error message 'Invalid    ║
║  credentials', but got 'Login failed'               ║
║                                                      ║
║  Stack Trace:                                        ║
║  File "login_steps.py", line 74                     ║
║    assert expected_message in actual_message         ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  📎 Attachments:                                     ║
║  📷 Failure Screenshot                               ║
║     [Click to view full screenshot]                  ║
║     ┌─────────────────────────────┐                 ║
║     │ [Screenshot preview]         │                 ║
║     │ Shows the error on screen    │                 ║
║     └─────────────────────────────┘                 ║
╚══════════════════════════════════════════════════════╝
```

---

## 📊 Timeline View

Visual representation of test execution:

```
Timeline
──────────────────────────────────────────────────────

Thread 1: ████████░░░░░░░░░░░░░░░░░░░░  (30s)
          Login Tests

Thread 1: ░░░░░░░░░░████████████░░░░░░  (28s)
          Search Tests

Thread 1: ░░░░░░░░░░░░░░░░░░████████░░  (22s)
          Asset Tests

0s        10s       20s       30s       40s
```

---

## 🏷️ Categories View

Test failures grouped by category:

```
╔══════════════════════════════════════════════════════╗
║  Failure Categories                                  ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  🔴 Product Defects (2 tests)                       ║
║     - Assertion failures                            ║
║     - Expected behavior not matching               ║
║                                                      ║
║  🟡 Element Not Found (1 test)                      ║
║     - Locator issues                                ║
║     - Page structure changed                        ║
║                                                      ║
║  🟠 Timeout Issues (1 test)                         ║
║     - Slow page load                                ║
║     - Element taking too long                       ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

---

## 📦 Behaviors View

Tests organized by Epic → Feature → Story:

```
📚 Epic: Authentication
  │
  ├─ 📖 Feature: Login
  │   ├─ 📝 Story: User Login
  │   │   ├─ ✅ Login with valid credentials
  │   │   └─ ✅ Login with different roles
  │   │
  │   └─ 📝 Story: Error Handling
  │       ├─ ✅ Login with invalid credentials
  │       └─ ✅ Login with empty fields
  │
  └─ 📖 Feature: Logout
      └─ 📝 Story: User Logout
          └─ ⚪ Logout successfully (not run)
```

---

## 📈 Historical Trends

When history is enabled, you see trends:

```
Test Execution Trend (Last 7 Runs)

Pass Rate:
100% ██████████████████████████  Run 7 (Latest)
 95% ███████████████████████░░  Run 6
 92% █████████████████████░░░░  Run 5
 88% ███████████████████░░░░░░  Run 4
 85% █████████████████░░░░░░░░  Run 3
 90% ██████████████████░░░░░░░  Run 2
 87% ████████████████░░░░░░░░░  Run 1

Trend: 📈 Improving
```

---

## 🌐 Environment Info

Environment details displayed in report:

```
╔══════════════════════════════════════════════════════╗
║  Test Environment                                    ║
╠══════════════════════════════════════════════════════╣
║  Browser: Chrome 120.0                               ║
║  Base URL: https://elasticm2m-dev.app.em2m.net      ║
║  Environment: Development                            ║
║  OS: Windows 11                                      ║
║  Python Version: 3.11                                ║
║  Test Run: December 31, 2024 14:39:00              ║
╚══════════════════════════════════════════════════════╝
```

---

## 🎯 Real Example Output

After running `generate_report.bat`, you'll see:

```bash
========================================
EM2M Test Automation - Report Generation
========================================

Running tests...
Test suite initialization complete
Feature: Search Functionality
  Scenario: Search for ASEED and select exact match
    ✓ Given the user is logged in
    ✓ When the user clicks the search button
    ✓ And the user enters "ASEED"
    ✓ Then dropdown should appear
    ✓ When clicks on exact match
    ✓ Then on ASEED details page

1 feature passed, 0 failed
7 steps passed, 0 failed
Took 0min 28.746s

Generating Allure report...
Report successfully generated to allure-report

Opening report in browser...
Serving reports from: http://localhost:50123
Press Ctrl+C to exit
```

Then your browser opens showing the beautiful Allure report!

---

## 📱 Mobile-Responsive

The report is mobile-friendly and can be viewed on:
- 💻 Desktop browsers
- 📱 Tablets
- 📱 Mobile phones

---

## 🎨 Color Coding

- 🟢 **Green** - Passed tests
- 🔴 **Red** - Failed tests
- ⚪ **Gray** - Skipped tests
- 🟡 **Yellow** - Broken tests (setup/teardown issues)
- 🔵 **Blue** - Unknown/Pending

---

## 💡 Pro Tips

1. **Click on any chart** - Interactive drill-down
2. **Use filters** - Filter by status, feature, tags
3. **Search** - Find specific tests quickly
4. **Export** - Download report data as JSON
5. **Share** - Copy shareable URL

---

**See your actual report by running:**
```bash
# Windows
generate_report.bat

# Linux/Mac
./generate_report.sh
```

The report will be better than these text examples! 🎉
