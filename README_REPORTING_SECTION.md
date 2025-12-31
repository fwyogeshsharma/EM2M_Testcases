# ADD THIS SECTION TO README.md

## 📊 Test Reporting

This project includes **Allure Reports** - a beautiful, interactive reporting framework.

### Features
- ✅ **Visual Dashboard** with charts and graphs
- ✅ **Pass/Fail Percentages** with trend analysis
- ✅ **Screenshots** automatically attached to failed tests
- ✅ **Detailed Test Steps** with execution logs
- ✅ **Historical Trends** to track test stability
- ✅ **Beautiful UI** that's easy to share

### Quick Start

**Generate Report (After Installing Allure):**
```bash
# Windows
generate_report.bat

# Linux/Mac
./generate_report.sh
```

**View Existing Report:**
```bash
# Windows
view_report.bat

# Linux/Mac
./view_report.sh
```

### Installation

**Install Allure CLI:**

```bash
# Windows (using Scoop)
scoop install allure

# Mac
brew install allure

# Linux
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
tar -zxvf allure-2.24.0.tgz -C /opt/
sudo ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure
```

**Detailed Installation Guide:** See [ALLURE_INSTALLATION.md](ALLURE_INSTALLATION.md)

### Manual Report Generation

```bash
# Step 1: Run tests with Allure formatter
behave -f allure_behave.formatter:AllureFormatter -o allure-results

# Step 2: Generate HTML report
allure generate allure-results --clean -o allure-report

# Step 3: Open in browser
allure open allure-report
```

### Report Documentation
- 📘 [REPORTING_GUIDE.md](REPORTING_GUIDE.md) - Complete reporting guide
- 📗 [ALLURE_INSTALLATION.md](ALLURE_INSTALLATION.md) - Installation instructions
- 📙 [REPORT_EXAMPLES.md](REPORT_EXAMPLES.md) - Visual examples of reports

### Sample Report Metrics

```
Total Tests: 7
Passed: 7 (100%)
Failed: 0 (0%)
Skipped: 0 (0%)

Pass Rate: 100%
Duration: 3m 45s
```

### Report Features

1. **Overview Dashboard**
   - Total tests count
   - Pass/Fail pie charts
   - Execution timeline

2. **Detailed Test Results**
   - Step-by-step execution
   - Console outputs
   - Screenshots on failures

3. **Trends & History**
   - Pass rate trends
   - Flaky test detection
   - Performance metrics

4. **Categorization**
   - By feature/epic/story
   - By severity
   - By failure category

---

