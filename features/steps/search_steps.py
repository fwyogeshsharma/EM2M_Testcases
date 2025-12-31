"""
Step definitions for search feature.
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from config.config import Config
import time


@given('the user is logged in with valid credentials')
def step_user_logged_in_with_credentials(context):
    """Ensure user is logged in with valid credentials."""
    # Navigate to login page
    login_page = LoginPage(context.driver)
    login_page.navigate_to_login()

    # Perform login
    login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)

    # Wait for page to load after login
    time.sleep(8)  # Increased wait time for page to fully load

    # Wait for page to be ready
    WebDriverWait(context.driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Initialize search page
    context.search_page = SearchPage(context.driver)


@when('the user clicks the search button in the navbar')
def step_click_search_button(context):
    """Click the search button in the navbar."""
    if not hasattr(context, 'search_page'):
        context.search_page = SearchPage(context.driver)

    context.search_page.click_search_button()
    time.sleep(1)  # Wait for search input to appear


@when('the user enters "{search_term}" in the search input field')
def step_enter_search_term(context, search_term):
    """Enter text in the search input field."""
    context.search_page.enter_search_term(search_term)
    context.search_term = search_term
    time.sleep(1)  # Wait for typing to complete


@when('the user waits for the dropdown to appear')
def step_wait_for_dropdown(context):
    """Wait for the search dropdown to appear."""
    context.search_page.wait_for_dropdown(timeout=10)


@then('the user should see "{text}" in the dropdown')
def step_verify_text_in_dropdown(context, text):
    """Verify specific text appears in the dropdown."""
    assert context.search_page.is_text_in_dropdown(text), \
        f"Text '{text}' not found in dropdown options"


@then('the dropdown should display matching results')
def step_verify_dropdown_displays_results(context):
    """Verify that the dropdown displays results."""
    assert context.search_page.is_dropdown_visible(), \
        "Search dropdown is not visible"

    options = context.search_page.get_dropdown_options()
    assert len(options) > 0, "No results found in dropdown"


@then('the dropdown should contain "{text}"')
def step_verify_dropdown_contains_text(context, text):
    """Verify dropdown contains specific text."""
    assert context.search_page.is_text_in_dropdown(text), \
        f"Dropdown does not contain '{text}'"


@when('the user clicks on the exact match "{text}"')
def step_click_exact_match(context, text):
    """Click on the exact match from dropdown."""
    context.search_page.click_exact_match(text)
    time.sleep(2)  # Wait for navigation


@then('the user should be on the ASEED details page')
def step_verify_aseed_details_page(context):
    """Verify user is on the ASEED details page."""
    # Wait for page to load
    time.sleep(2)

    # Get current URL
    current_url = context.driver.current_url

    # Check if URL changed to an org details page (ASEED's org ID page)
    # The URL will be something like /org/d1609db2-2f95-461c-bcd8-9338d07e48b9
    assert '/org/' in current_url or 'ASEED' in current_url or '/item/' in current_url, \
        f"Expected to be on ASEED details page, but current URL is: {current_url}"

    print(f"Successfully navigated to ASEED details page: {current_url}")


@when('the user performs a complete search for "{search_term}"')
def step_complete_search_flow(context, search_term):
    """Perform complete search: click button, enter text, select match."""
    context.search_page.search_and_select(search_term)
    context.search_term = search_term
