"""
Helper script to inspect search elements after login.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')

# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    print("\n" + "="*80)
    print("INSPECTING SEARCH ELEMENTS AFTER LOGIN")
    print("="*80 + "\n")

    # Login first
    print("Logging in...")
    driver.get("https://elasticm2m-dev.app.em2m.net/login")
    time.sleep(3)

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("divya.bika@faberwork.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Testfaber123!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.form-login-button")
    login_button.click()

    print("Waiting for page to load after login...")
    time.sleep(10)  # Increased wait time

    print(f"Current URL after login: {driver.current_url}\n")

    # Wait for the page to fully load
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    print("-" * 80)
    print("SEARCHING FOR SEARCH BUTTON")
    print("-" * 80)

    # Find elements with mat-mdc-button-touch-target class
    touch_targets = driver.find_elements(By.CSS_SELECTOR, ".mat-mdc-button-touch-target")
    print(f"\nFound {len(touch_targets)} elements with class 'mat-mdc-button-touch-target'\n")

    # Find all buttons
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Found {len(buttons)} total buttons on the page")

    # If no buttons found, let's search for all clickable elements
    if len(buttons) == 0:
        print("\nNo buttons found. Searching for all elements...")
        all_elements = driver.find_elements(By.CSS_SELECTOR, "*")
        print(f"Found {len(all_elements)} total elements")

        # Check if page has loaded
        body_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"\nPage body text length: {len(body_text)}")
        print(f"First 200 characters: {body_text[:200]}")
        print()

    print()

    # Find buttons with search-related attributes
    search_buttons = []
    for i, btn in enumerate(buttons, 1):
        btn_text = btn.text.strip()
        btn_class = btn.get_attribute('class')
        btn_aria = btn.get_attribute('aria-label')

        if 'search' in btn_text.lower() or \
           (btn_aria and 'search' in btn_aria.lower()) or \
           'search' in btn_class.lower():
            search_buttons.append(btn)
            print(f"Search Button #{len(search_buttons)}:")
            print(f"  Text: {btn_text}")
            print(f"  Class: {btn_class}")
            print(f"  Aria-label: {btn_aria}")
            print()

    if search_buttons:
        print(f"\nFound {len(search_buttons)} potential search button(s)")
        print("\nAttempting to click the first search button...")
        search_buttons[0].click()
        time.sleep(2)

        print("\n" + "-" * 80)
        print("SEARCHING FOR SEARCH INPUT FIELD")
        print("-" * 80)

        # Find input fields that appeared
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"\nFound {len(inputs)} input fields:\n")

        for i, inp in enumerate(inputs, 1):
            if inp.is_displayed():
                print(f"Visible Input #{i}:")
                print(f"  Type: {inp.get_attribute('type')}")
                print(f"  ID: {inp.get_attribute('id')}")
                print(f"  Name: {inp.get_attribute('name')}")
                print(f"  Class: {inp.get_attribute('class')}")
                print(f"  Placeholder: {inp.get_attribute('placeholder')}")
                print(f"  Aria-label: {inp.get_attribute('aria-label')}")
                print()

        # Try to type in the search field
        print("Attempting to enter 'ASEED' in search field...")
        visible_inputs = [inp for inp in inputs if inp.is_displayed()]
        if visible_inputs:
            visible_inputs[0].send_keys("ASEED")
            time.sleep(3)

            print("\n" + "-" * 80)
            print("SEARCHING FOR DROPDOWN/AUTOCOMPLETE")
            print("-" * 80)

            # Find dropdown elements
            dropdowns = driver.find_elements(By.CSS_SELECTOR, ".mat-autocomplete-panel, .mat-option, [role='listbox'], [role='option']")
            print(f"\nFound {len(dropdowns)} potential dropdown elements\n")

            for i, dd in enumerate(dropdowns, 1):
                if dd.is_displayed():
                    print(f"Dropdown Element #{i}:")
                    print(f"  Tag: {dd.tag_name}")
                    print(f"  Class: {dd.get_attribute('class')}")
                    print(f"  Text: {dd.text}")
                    print(f"  Role: {dd.get_attribute('role')}")
                    print()

    print("\n" + "="*80)
    print("RECOMMENDED LOCATORS")
    print("="*80 + "\n")

    if search_buttons:
        btn = search_buttons[0]
        if btn.get_attribute('aria-label'):
            print(f"SEARCH_BUTTON = (By.CSS_SELECTOR, \"button[aria-label='{btn.get_attribute('aria-label')}']\")")
        else:
            print(f"SEARCH_BUTTON = (By.CSS_SELECTOR, \".mat-mdc-button-touch-target\")")

    print("\nBrowser will remain open for 30 seconds for manual inspection...")
    time.sleep(30)

except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    time.sleep(10)

finally:
    driver.quit()
    print("\nBrowser closed.")
