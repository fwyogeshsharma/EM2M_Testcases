# Allure Installation Guide

## 📦 Installing Allure Command Line Tool

Allure CLI is required to generate and view beautiful HTML reports from test results.

---

## Windows Installation

### Method 1: Using Scoop (Recommended)

**Step 1: Install Scoop** (if not already installed)
```powershell
# Open PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

**Step 2: Install Allure**
```bash
scoop install allure
```

**Step 3: Verify Installation**
```bash
allure --version
```

### Method 2: Manual Installation

**Step 1: Download Allure**
- Go to: https://github.com/allure-framework/allure2/releases
- Download latest `allure-x.x.x.zip` file

**Step 2: Extract**
- Extract to `C:\allure` (or any location)

**Step 3: Add to PATH**
1. Right-click "This PC" → Properties → Advanced System Settings
2. Click "Environment Variables"
3. Under "System variables", find "Path" and click "Edit"
4. Click "New" and add: `C:\allure\bin`
5. Click "OK" to save

**Step 4: Verify**
```bash
# Open NEW command prompt
allure --version
```

---

## Mac Installation

### Using Homebrew (Recommended)

**Step 1: Install Homebrew** (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2: Install Allure**
```bash
brew install allure
```

**Step 3: Verify**
```bash
allure --version
```

---

## Linux Installation

### Ubuntu/Debian

**Step 1: Download Allure**
```bash
# Download latest version (check releases page for latest version)
wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
```

**Step 2: Extract**
```bash
sudo tar -zxvf allure-2.24.0.tgz -C /opt/
```

**Step 3: Create Symlink**
```bash
sudo ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure
```

**Step 4: Verify**
```bash
allure --version
```

### Using Package Manager

**For Debian/Ubuntu:**
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

**For Fedora/CentOS:**
```bash
sudo wget -O /etc/yum.repos.d/allure.repo https://dl.bintray.com/qameta/rpm/allure.repo
sudo yum install allure
```

---

## Verification

After installation, verify Allure is working:

```bash
# Check version
allure --version

# Should output something like:
# 2.24.0
```

---

## Troubleshooting

### Windows: "allure is not recognized"
**Solution:**
1. Verify PATH is set correctly
2. Restart Command Prompt/PowerShell
3. Try full path: `C:\allure\bin\allure --version`

### Mac: "command not found: allure"
**Solution:**
```bash
# Update Homebrew
brew update

# Reinstall Allure
brew reinstall allure

# Check PATH
echo $PATH
```

### Linux: Permission Denied
**Solution:**
```bash
# Make allure executable
sudo chmod +x /opt/allure-2.24.0/bin/allure

# Verify permissions
ls -la /usr/bin/allure
```

---

## Next Steps

Once Allure is installed, you can:

1. **Generate Reports:**
   ```bash
   # Windows
   generate_report.bat

   # Linux/Mac
   ./generate_report.sh
   ```

2. **View Reports:**
   ```bash
   # Windows
   view_report.bat

   # Linux/Mac
   ./view_report.sh
   ```

3. **Read Documentation:**
   - See `REPORTING_GUIDE.md` for detailed usage
   - See `README.md` for project overview

---

## Quick Test

After installation, test with:

```bash
# Run a test with Allure reporting
behave features/search.feature:10 -f allure_behave.formatter:AllureFormatter -o allure-results

# Generate and open report
allure serve allure-results
```

Your browser should open with a beautiful Allure report! 🎉

---

**Need Help?**
- Allure Docs: https://docs.qameta.io/allure/
- Allure Releases: https://github.com/allure-framework/allure2/releases
- Report Issues: See project README
