"""
Script to inspect search dropdown after typing ASEED.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to login page
    driver.get("https://elasticm2m-dev.app.em2m.net/login")
    print("Navigated to login page")
    time.sleep(5)

    # Wait for page to load
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Login
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("divya.bika@faberwork.com")
    password_field.send_keys("Testfaber123!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.form-login-button")
    login_button.click()
    print("Clicked login button")

    # Wait for page to load
    time.sleep(8)

    print("\n--- After Login ---")
    print(f"Current URL: {driver.current_url}")

    # Find the search button with mat-mdc-button-touch-target class
    print("\n--- Looking for search button ---")

    # Try to find buttons with the touch target class
    buttons = driver.find_elements(By.CSS_SELECTOR, "button")
    for i, button in enumerate(buttons):
        touch_targets = button.find_elements(By.CSS_SELECTOR, ".mat-mdc-button-touch-target")
        if touch_targets:
            print(f"Button {i}: has touch-target, text='{button.text}', aria-label='{button.get_attribute('aria-label')}'")

    # Click the search button (looking for one with search text or icon)
    search_button = None
    for button in buttons:
        touch_targets = button.find_elements(By.CSS_SELECTOR, ".mat-mdc-button-touch-target")
        if touch_targets and ('search' in button.text.lower() or
                              'search' in str(button.get_attribute('aria-label')).lower()):
            search_button = button
            break

    if search_button:
        print(f"\nFound search button: {search_button.text}")
        search_button.click()
        print("Clicked search button")
        time.sleep(2)
    else:
        print("\nSearch button not found, trying alternative approach...")
        # Try finding by icon
        search_buttons = driver.find_elements(By.XPATH, "//button[.//mat-icon[contains(text(), 'search')]]")
        if search_buttons:
            search_buttons[0].click()
            print("Clicked search button via icon")
            time.sleep(2)

    # Look for search input field
    print("\n--- Looking for search input ---")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        if inp.is_displayed():
            print(f"Visible Input {i}: type='{inp.get_attribute('type')}', "
                  f"placeholder='{inp.get_attribute('placeholder')}', "
                  f"class='{inp.get_attribute('class')}'")

    # Type ASEED in the search input
    search_input = None
    for inp in inputs:
        if inp.is_displayed() and inp.get_attribute('type') in ['text', 'search', None]:
            placeholder = inp.get_attribute('placeholder')
            if placeholder and 'search' in placeholder.lower():
                search_input = inp
                break

    if not search_input:
        # Try any visible text input
        for inp in inputs:
            if inp.is_displayed() and inp.get_attribute('type') in ['text', 'search', None]:
                search_input = inp
                break

    if search_input:
        print(f"\nFound search input: {search_input.get_attribute('placeholder')}")
        search_input.send_keys("ASEED")
        print("Typed 'ASEED' in search input")
        time.sleep(3)  # Wait for dropdown to appear
    else:
        print("\nSearch input not found!")

    # Inspect what dropdown elements appear
    print("\n--- Inspecting dropdown elements ---")

    # Look for autocomplete panels
    autocomplete_panels = driver.find_elements(By.CSS_SELECTOR, ".mat-mdc-autocomplete-panel, .mat-autocomplete-panel, [role='listbox']")
    print(f"Found {len(autocomplete_panels)} autocomplete panels")
    for i, panel in enumerate(autocomplete_panels):
        if panel.is_displayed():
            print(f"\nPanel {i} is visible:")
            print(f"  Class: {panel.get_attribute('class')}")
            print(f"  Role: {panel.get_attribute('role')}")

    # Look for mat-options
    options = driver.find_elements(By.CSS_SELECTOR, "mat-option, .mat-mdc-option, [role='option']")
    print(f"\nFound {len(options)} mat-options")
    for i, option in enumerate(options):
        if option.is_displayed():
            print(f"  Option {i}: text='{option.text}', class='{option.get_attribute('class')}'")

    # Look for any dropdown/list elements
    dropdowns = driver.find_elements(By.CSS_SELECTOR, "[role='listbox'], .dropdown-menu, .dropdown, ul[class*='dropdown']")
    print(f"\nFound {len(dropdowns)} dropdown-like elements")
    for i, dd in enumerate(dropdowns):
        if dd.is_displayed():
            print(f"  Dropdown {i}: class='{dd.get_attribute('class')}', role='{dd.get_attribute('role')}'")

    print("\n--- Page Source (snippet) ---")
    page_source = driver.page_source
    if 'ASEED' in page_source:
        # Find the context around ASEED in the page source
        idx = page_source.find('ASEED')
        print(page_source[max(0, idx-200):min(len(page_source), idx+200)])

    print("\n\n=== PAUSING FOR 30 SECONDS - CHECK THE BROWSER ===")
    time.sleep(30)

except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()

finally:
    print("\nClosing browser...")
    driver.quit()
