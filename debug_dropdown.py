"""
Debug script to see dropdown elements after typing ASEED.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Login
    driver.get("https://elasticm2m-dev.app.em2m.net/login")
    time.sleep(5)

    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("divya.bika@faberwork.com")
    password_field.send_keys("Testfaber123!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.form-login-button")
    login_button.click()
    print("Logged in")

    time.sleep(8)

    # Find search button (not burger menu)
    print("\n--- Looking for search button ---")
    search_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'search') or .//mat-icon[text()='search']]")
    print(f"Found {len(search_buttons)} search buttons")

    if search_buttons:
        print(f"Clicking search button")
        driver.execute_script("arguments[0].click();", search_buttons[0])
        time.sleep(2)
    else:
        print("No search button found, trying alternative...")
        # Try finding any button with search
        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in all_buttons:
            if 'search' in btn.get_attribute('aria-label', '').lower():
                driver.execute_script("arguments[0].click();", btn)
                print(f"Clicked button with aria-label: {btn.get_attribute('aria-label')}")
                time.sleep(2)
                break

    # Find and type in search input
    print("\n--- Looking for search input ---")
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input"))
    )
    print(f"Found search input: {search_input.get_attribute('class')}")

    # Type ASEED
    driver.execute_script("arguments[0].focus();", search_input)
    for char in "ASEED":
        search_input.send_keys(char)
        time.sleep(0.1)

    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", search_input)
    print("Typed 'ASEED'")

    time.sleep(3)

    # Look for ALL possible dropdown/overlay elements
    print("\n--- Looking for dropdown elements ---")

    # Check for cdk-overlay-pane
    overlays = driver.find_elements(By.CSS_SELECTOR, ".cdk-overlay-pane")
    print(f"Found {len(overlays)} cdk-overlay-pane elements")
    for i, overlay in enumerate(overlays):
        if overlay.is_displayed():
            print(f"  Overlay {i} is visible, class: {overlay.get_attribute('class')}")

    # Check for autocomplete panels
    autocomplete = driver.find_elements(By.CSS_SELECTOR, "[role='listbox'], .mat-autocomplete-panel, .mat-mdc-autocomplete-panel")
    print(f"Found {len(autocomplete)} autocomplete panel elements")
    for i, panel in enumerate(autocomplete):
        if panel.is_displayed():
            print(f"  Panel {i} is visible, class: {panel.get_attribute('class')}, role: {panel.get_attribute('role')}")

    # Check for mat-options
    options = driver.find_elements(By.CSS_SELECTOR, "mat-option, .mat-mdc-option, [role='option']")
    print(f"Found {len(options)} option elements")
    for i, opt in enumerate(options):
        if opt.is_displayed():
            print(f"  Option {i}: text='{opt.text}', class='{opt.get_attribute('class')}'")

    # Check page source for ASEED
    print("\n--- Checking page source for dropdown HTML ---")
    page_source = driver.page_source
    if 'ASEED' in page_source:
        # Find all occurrences
        import re
        matches = list(re.finditer(r'.{50}ASEED.{50}', page_source, re.IGNORECASE))
        print(f"Found {len(matches)} occurrences of 'ASEED' in page")
        for i, match in enumerate(matches[:3]):  # Show first 3
            print(f"  Match {i}: ...{match.group()}...")

    print("\n\n=== PAUSING FOR 60 SECONDS - INSPECT THE BROWSER ===")
    time.sleep(60)

except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
    time.sleep(10)

finally:
    driver.quit()
