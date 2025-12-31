"""
Helper script to check where the page redirects after login.
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
    print("CHECKING LOGIN REDIRECT")
    print("="*80 + "\n")

    # Navigate to login page
    url = "https://elasticm2m-dev.app.em2m.net/login"
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(3)

    print(f"Current URL: {driver.current_url}\n")

    # Enter credentials
    print("Entering credentials...")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("divya.bika@faberwork.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Testfaber123!")

    print("Credentials entered. Clicking LOGIN button...")

    # Click login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button.form-login-button")
    login_button.click()

    # Wait for redirect
    print("Waiting for redirect...\n")
    time.sleep(5)

    print("-" * 80)
    print("AFTER LOGIN:")
    print("-" * 80)
    print(f"Current URL: {driver.current_url}")
    print(f"Page Title: {driver.title}")
    print("-" * 80)

    # Check what part of URL to use for assertion
    from urllib.parse import urlparse
    parsed_url = urlparse(driver.current_url)
    print(f"\nURL Path: {parsed_url.path}")
    print(f"URL Fragment: {parsed_url.fragment}")

    print("\n" + "="*80)
    print("RECOMMENDED UPDATE FOR STEP DEFINITION:")
    print("="*80)

    if '/dashboard' in driver.current_url:
        print("\nURL contains '/dashboard' - No change needed!")
    elif parsed_url.path != '/login':
        print(f"\nUpdate the assertion to check for: '{parsed_url.path}'")
        print(f"Or check if URL changed from login: assert '/login' not in url")
    else:
        print("\nURL did not change - Login may have failed!")
        print("Check for error messages on the page...")

    print("\nBrowser will remain open for 20 seconds for inspection...")
    time.sleep(20)

except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
    time.sleep(10)

finally:
    driver.quit()
    print("\nBrowser closed.")
