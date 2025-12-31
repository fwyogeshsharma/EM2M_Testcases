"""
Script to find the correct search button and input on navbar.
"""
# -*- coding: utf-8 -*-

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
    print(" Logged in successfully")

    time.sleep(8)

    print("\n=== STEP 1: Finding search button on navbar ===")

    # Look for all buttons on the page
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Total buttons found: {len(all_buttons)}")

    print("\nButtons in navbar area (checking visible buttons):")
    for i, btn in enumerate(all_buttons):
        if btn.is_displayed():
            aria_label = btn.get_attribute('aria-label') or ''
            btn_text = btn.text.strip()
            btn_class = btn.get_attribute('class')

            # Check if it's likely a search button
            if 'search' in aria_label.lower() or 'search' in btn_text.lower():
                print(f"\n SEARCH BUTTON FOUND - Button {i}:")
                print(f"   Text: '{btn_text}'")
                print(f"   Aria-label: '{aria_label}'")
                print(f"   Class: '{btn_class}'")
                print(f"   HTML: {btn.get_attribute('outerHTML')[:200]}")

    # Count visible inputs BEFORE clicking
    inputs_before = driver.find_elements(By.TAG_NAME, "input")
    visible_inputs_before = [inp for inp in inputs_before if inp.is_displayed()]
    print(f"\n Visible inputs BEFORE clicking search: {len(visible_inputs_before)}")

    print("\n=== STEP 2: Clicking the search button ===")

    # Find and click the search button
    search_button = None
    for btn in all_buttons:
        aria_label = btn.get_attribute('aria-label') or ''
        btn_text = btn.text.strip().lower()

        if ('search' in aria_label.lower() or 'search' in btn_text) and btn.is_displayed():
            search_button = btn
            print(f"Clicking search button with text: '{btn.text}', aria-label: '{aria_label}'")
            break

    if search_button:
        driver.execute_script("arguments[0].click();", search_button)
        print(" Search button clicked")
        time.sleep(2)
    else:
        print(" No search button found!")
        raise Exception("Cannot find search button")

    print("\n=== STEP 3: Finding the NEW search input that appeared ===")

    # Count visible inputs AFTER clicking
    inputs_after = driver.find_elements(By.TAG_NAME, "input")
    visible_inputs_after = [inp for inp in inputs_after if inp.is_displayed()]
    print(f" Visible inputs AFTER clicking search: {len(visible_inputs_after)}")

    # Find the NEW input (that wasn't there before)
    new_inputs = [inp for inp in visible_inputs_after if inp not in visible_inputs_before]

    if new_inputs:
        print(f"\n Found {len(new_inputs)} NEW input(s) that appeared:")
        for i, inp in enumerate(new_inputs):
            print(f"\n   New Input {i}:")
            print(f"      Type: {inp.get_attribute('type')}")
            print(f"      Class: {inp.get_attribute('class')}")
            print(f"      Placeholder: {inp.get_attribute('placeholder')}")
            print(f"      Name: {inp.get_attribute('name')}")
            print(f"      ID: {inp.get_attribute('id')}")
            print(f"      HTML: {inp.get_attribute('outerHTML')[:200]}")

    # Use the first new input (or last visible input)
    search_input = new_inputs[0] if new_inputs else visible_inputs_after[-1]

    print(f"\n=== STEP 4: Typing 'ASEED' in the search input ===")
    print(f"Using input with class: {search_input.get_attribute('class')}")

    driver.execute_script("arguments[0].focus();", search_input)
    driver.execute_script("arguments[0].value = '';", search_input)

    for char in "ASEED":
        search_input.send_keys(char)
        time.sleep(0.15)

    # Trigger input event
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", search_input)
    driver.execute_script("arguments[0].dispatchEvent(new Event('keyup', { bubbles: true }));", search_input)

    print(" Typed 'ASEED'")

    print("\n=== STEP 5: Waiting for dropdown to appear ===")
    time.sleep(3)

    # Look for dropdown elements
    print("\nSearching for dropdown elements:")

    # Method 1: Look for overlay panes
    overlays = driver.find_elements(By.CSS_SELECTOR, ".cdk-overlay-pane, .cdk-overlay-container *")
    visible_overlays = [o for o in overlays if o.is_displayed()]
    print(f"  - cdk-overlay elements: {len(visible_overlays)} visible")

    # Method 2: Look for autocomplete panels
    autocomplete_panels = driver.find_elements(By.CSS_SELECTOR, "[class*='autocomplete'], [class*='dropdown']")
    visible_autocomplete = [a for a in autocomplete_panels if a.is_displayed()]
    print(f"  - autocomplete/dropdown elements: {len(visible_autocomplete)} visible")

    # Method 3: Look for mat-options
    mat_options = driver.find_elements(By.CSS_SELECTOR, "mat-option, [role='option'], .mat-option, .mat-mdc-option")
    visible_options = [o for o in mat_options if o.is_displayed()]
    print(f"  - option elements: {len(visible_options)} visible")

    if visible_options:
        print(f"\n SUCCESS! Found {len(visible_options)} dropdown options:")
        for i, opt in enumerate(visible_options[:5]):  # Show first 5
            print(f"   Option {i}: '{opt.text}' (class: {opt.get_attribute('class')})")

    # Method 4: Check page source around "ASEED"
    page_source = driver.page_source
    if 'ASEED' in page_source:
        import re
        # Look for dropdown-like structures containing ASEED
        patterns = [
            r'<mat-option[^>]*>.*?ASEED.*?</mat-option>',
            r'<div[^>]*option[^>]*>.*?ASEED.*?</div>',
            r'<li[^>]*>.*?ASEED.*?</li>',
        ]

        print("\n HTML structures containing 'ASEED':")
        for pattern in patterns:
            matches = re.findall(pattern, page_source, re.IGNORECASE | re.DOTALL)
            if matches:
                print(f"\n   Pattern '{pattern[:30]}...' found {len(matches)} times:")
                for match in matches[:2]:
                    print(f"      {match[:150]}...")

    # Take a screenshot
    screenshot_path = "E:\\Projects\\EM2M_Testcases\\dropdown_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"\n Screenshot saved to: {screenshot_path}")

    print("\n\n=== PAUSING FOR 60 SECONDS - PLEASE INSPECT THE BROWSER ===")
    print("Check if the dropdown is visible with 'ASEED' in it")
    time.sleep(60)

except Exception as e:
    print(f"\n Error: {e}")
    import traceback
    traceback.print_exc()

    # Save error screenshot
    try:
        driver.save_screenshot("E:\\Projects\\EM2M_Testcases\\error_screenshot.png")
        print("Error screenshot saved")
    except:
        pass

    time.sleep(10)

finally:
    driver.quit()
    print("\n Browser closed")
