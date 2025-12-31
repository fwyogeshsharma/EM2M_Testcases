#!/usr/bin/env python3
"""
Verification script to check project structure.
Run this to ensure all required files are in place.
"""

import os
import sys

# Define expected structure
REQUIRED_FILES = {
    'Features': [
        'features/login.feature',
        'features/search.feature',
        'features/assets.feature',
        'features/environment.py',
    ],
    'Step Definitions': [
        'features/steps/__init__.py',
        'features/steps/login_steps.py',
        'features/steps/search_steps.py',
        'features/steps/assets_steps.py',
        'features/steps/common_steps.py',
    ],
    'Page Objects': [
        'pages/__init__.py',
        'pages/base_page.py',
        'pages/login_page.py',
        'pages/search_page.py',
        'pages/assets_page.py',
    ],
    'Configuration': [
        'config/__init__.py',
        'config/config.py',
        '.env.example',
        'behave.ini',
    ],
    'Utilities': [
        'utilities/__init__.py',
        'utilities/helpers.py',
    ],
    'Documentation': [
        'README.md',
        'SETUP_GUIDE.md',
        'PROJECT_STRUCTURE.md',
        'TEST_SUMMARY.md',
        'QUICK_REFERENCE.md',
        'REPORTING_GUIDE.md',
        'ALLURE_INSTALLATION.md',
        'REPORT_EXAMPLES.md',
        'REPORTING_SUMMARY.md',
    ],
    'Scripts': [
        'requirements.txt',
        'run_tests.bat',
        'run_tests.sh',
        'cleanup.bat',
        'cleanup.sh',
        'generate_report.bat',
        'generate_report.sh',
        'view_report.bat',
        'view_report.sh',
        'run_tests_with_report.bat',
    ],
    'Configuration': [
        'allure.properties',
    ],
}

REQUIRED_DIRS = [
    'features',
    'features/steps',
    'pages',
    'config',
    'utilities',
    'reports',
]

def check_files():
    """Check if all required files exist."""
    print("=" * 80)
    print("EM2M Test Automation - Structure Verification")
    print("=" * 80)

    all_good = True
    missing_files = []

    for category, files in REQUIRED_FILES.items():
        print(f"\n{category}:")
        for file_path in files:
            if os.path.exists(file_path):
                print(f"  [OK] {file_path}")
            else:
                print(f"  [MISSING] {file_path}")
                all_good = False
                missing_files.append(file_path)

    print("\nDirectories:")
    for dir_path in REQUIRED_DIRS:
        if os.path.isdir(dir_path):
            print(f"  [OK] {dir_path}/")
        else:
            print(f"  [MISSING] {dir_path}/")
            all_good = False

    print("\n" + "=" * 80)

    if all_good:
        print("[SUCCESS] ALL CHECKS PASSED - Project structure is correct!")
        print("=" * 80)
        return 0
    else:
        print("[ERROR] SOME FILES ARE MISSING!")
        print("\nMissing files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        print("=" * 80)
        return 1

def check_imports():
    """Check if key Python modules can be imported."""
    print("\nChecking Python Dependencies:")

    dependencies = [
        'selenium',
        'behave',
        'webdriver_manager',
        'dotenv',
    ]

    all_good = True
    for module in dependencies:
        try:
            __import__(module)
            print(f"  [OK] {module}")
        except ImportError:
            print(f"  [MISSING] {module} - NOT INSTALLED!")
            all_good = False

    if not all_good:
        print("\n[WARNING] Install missing dependencies with:")
        print("  pip install -r requirements.txt")

    return all_good

def count_tests():
    """Count test scenarios in feature files."""
    print("\nTest Scenario Count:")

    total_scenarios = 0
    for feature_file in ['features/login.feature', 'features/search.feature', 'features/assets.feature']:
        if os.path.exists(feature_file):
            with open(feature_file, 'r', encoding='utf-8') as f:
                content = f.read()
                count = content.count('Scenario:') + content.count('Scenario Outline:')
                print(f"  {feature_file}: {count} scenarios")
                total_scenarios += count

    print(f"\nTotal: {total_scenarios} test scenarios")
    return total_scenarios

if __name__ == '__main__':
    print()

    # Check file structure
    structure_ok = check_files() == 0

    # Check dependencies
    deps_ok = check_imports()

    # Count tests
    test_count = count_tests()

    print("\n" + "=" * 80)
    if structure_ok and deps_ok:
        print("[SUCCESS] PROJECT VERIFICATION COMPLETE - READY TO RUN TESTS!")
        print("\nQuick Start:")
        print("  1. Copy .env.example to .env and add your credentials")
        print("  2. Run tests: behave")
        print("  3. Run smoke tests: behave --tags=@smoke")
    else:
        print("[WARNING] SETUP INCOMPLETE - Please fix the issues above")
        sys.exit(1)

    print("=" * 80)
    print()
