"""
Common step definitions that can be reused across features.
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from config.config import Config
import time


@given('the user navigates to "{url}"')
def step_navigate_to_url(context, url):
    """Navigate to a specific URL."""
    if url.startswith('http'):
        context.driver.get(url)
    else:
        context.driver.get(f"{context.base_url}{url}")


@when('the user waits for {seconds:d} seconds')
def step_wait_for_seconds(context, seconds):
    """Wait for a specified number of seconds."""
    import time
    time.sleep(seconds)


@when('the user clicks on element with selector "{selector}"')
def step_click_element_by_selector(context, selector):
    """Click on an element identified by CSS selector."""
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    element.click()


@when('the user enters "{text}" into field with selector "{selector}"')
def step_enter_text_by_selector(context, text, selector):
    """Enter text into an input field identified by CSS selector."""
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    element.clear()
    element.send_keys(text)


@then('the element with selector "{selector}" should be visible')
def step_verify_element_visible(context, selector):
    """Verify an element is visible."""
    element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )
    assert element.is_displayed(), f"Element with selector '{selector}' is not visible"


@then('the element with selector "{selector}" should contain text "{expected_text}"')
def step_verify_element_text(context, selector, expected_text):
    """Verify an element contains specific text."""
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    actual_text = element.text
    assert expected_text in actual_text, \
        f"Expected text '{expected_text}' not found in '{actual_text}'"


@then('the page title should be "{expected_title}"')
def step_verify_page_title(context, expected_title):
    """Verify the page title."""
    actual_title = context.driver.title
    assert expected_title == actual_title, \
        f"Expected title '{expected_title}', but got '{actual_title}'"


@then('the current URL should contain "{expected_url_part}"')
def step_verify_url_contains(context, expected_url_part):
    """Verify the current URL contains a specific part."""
    current_url = context.driver.current_url
    assert expected_url_part in current_url, \
        f"Expected URL to contain '{expected_url_part}', but got '{current_url}'"


@given('the user is logged in with valid credentials')
def step_user_logged_in_with_valid_credentials(context):
    """Ensure user is logged in with valid credentials."""
    login_page = LoginPage(context.driver)
    login_page.navigate_to_login()
    login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)

    # Wait for page to load after login
    time.sleep(8)  # Increased wait time for page to fully load

    # Wait for page to be ready
    WebDriverWait(context.driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Initialize search page for search tests
    context.search_page = SearchPage(context.driver)
