"""
Helper script to inspect the login page and find element locators.
This will open the browser and print out information about login form elements.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Comment out to see the browser
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
    print("INSPECTING LOGIN PAGE")
    print("="*80 + "\n")

    # Navigate to login page
    url = "https://elasticm2m-dev.app.em2m.net/login"
    print(f"Navigating to: {url}")
    driver.get(url)

    # Wait for page to load
    time.sleep(5)

    print(f"\nCurrent URL: {driver.current_url}")
    print(f"Page Title: {driver.title}\n")

    print("-" * 80)
    print("SEARCHING FOR INPUT FIELDS")
    print("-" * 80)

    # Find all input elements
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\nFound {len(inputs)} input elements:\n")

    for i, input_elem in enumerate(inputs, 1):
        input_type = input_elem.get_attribute('type')
        input_id = input_elem.get_attribute('id')
        input_name = input_elem.get_attribute('name')
        input_class = input_elem.get_attribute('class')
        input_placeholder = input_elem.get_attribute('placeholder')

        print(f"Input #{i}:")
        print(f"  Type: {input_type}")
        print(f"  ID: {input_id}")
        print(f"  Name: {input_name}")
        print(f"  Class: {input_class}")
        print(f"  Placeholder: {input_placeholder}")
        print()

    print("-" * 80)
    print("SEARCHING FOR BUTTONS")
    print("-" * 80)

    # Find all button elements
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"\nFound {len(buttons)} button elements:\n")

    for i, button in enumerate(buttons, 1):
        button_type = button.get_attribute('type')
        button_id = button.get_attribute('id')
        button_class = button.get_attribute('class')
        button_text = button.text

        print(f"Button #{i}:")
        print(f"  Type: {button_type}")
        print(f"  ID: {button_id}")
        print(f"  Class: {button_class}")
        print(f"  Text: {button_text}")
        print()

    print("-" * 80)
    print("RECOMMENDED LOCATORS FOR PAGE OBJECTS")
    print("-" * 80)
    print("\nBased on the elements found, update your pages/login_page.py with:\n")

    # Try to identify email/username field
    email_fields = [inp for inp in inputs if inp.get_attribute('type') in ['email', 'text']]
    if email_fields:
        elem = email_fields[0]
        if elem.get_attribute('id'):
            print(f"USERNAME_INPUT = (By.ID, '{elem.get_attribute('id')}')")
        elif elem.get_attribute('name'):
            print(f"USERNAME_INPUT = (By.NAME, '{elem.get_attribute('name')}')")
        else:
            print(f"USERNAME_INPUT = (By.CSS_SELECTOR, 'input[type=\"{elem.get_attribute('type')}\"]')")

    # Try to identify password field
    password_fields = [inp for inp in inputs if inp.get_attribute('type') == 'password']
    if password_fields:
        elem = password_fields[0]
        if elem.get_attribute('id'):
            print(f"PASSWORD_INPUT = (By.ID, '{elem.get_attribute('id')}')")
        elif elem.get_attribute('name'):
            print(f"PASSWORD_INPUT = (By.NAME, '{elem.get_attribute('name')}')")
        else:
            print(f"PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type=\"password\"]')")

    # Try to identify login button
    submit_buttons = [btn for btn in buttons if btn.get_attribute('type') == 'submit' or 'login' in btn.text.lower() or 'sign' in btn.text.lower()]
    if submit_buttons:
        elem = submit_buttons[0]
        if elem.get_attribute('id'):
            print(f"LOGIN_BUTTON = (By.ID, '{elem.get_attribute('id')}')")
        elif 'login' in elem.text.lower():
            print(f"LOGIN_BUTTON = (By.XPATH, \"//button[contains(text(), '{elem.text}')]\")")
        else:
            print(f"LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type=\"submit\"]')")

    print("\n" + "="*80)
    print("INSPECTION COMPLETE")
    print("="*80)

    print("\nBrowser will remain open for 30 seconds so you can manually inspect...")
    print("Press Ctrl+C to close immediately.")
    time.sleep(30)

except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
    print("\nBrowser closed.")
