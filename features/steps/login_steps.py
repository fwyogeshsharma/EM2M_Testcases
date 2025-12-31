"""
Step definitions for login feature.
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from config.config import Config


@given('the user is on the login page')
def step_navigate_to_login_page(context):
    """Navigate to the login page."""
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()


@when('the user enters valid username and password')
def step_enter_valid_credentials(context):
    """Enter valid login credentials."""
    context.login_page.enter_username(Config.TEST_USERNAME)
    context.login_page.enter_password(Config.TEST_PASSWORD)


@when('the user enters invalid username and password')
def step_enter_invalid_credentials(context):
    """Enter invalid login credentials."""
    context.login_page.enter_username('invalid@em2m.net')
    context.login_page.enter_password('wrongpassword')


@when('the user leaves username and password empty')
def step_leave_credentials_empty(context):
    """Leave username and password fields empty."""
    context.login_page.enter_username('')
    context.login_page.enter_password('')


@when('the user enters "{username}" and "{password}"')
def step_enter_specific_credentials(context, username, password):
    """Enter specific username and password."""
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when('the user clicks the login button')
def step_click_login_button(context):
    """Click the login button."""
    context.login_page.click_login_button()


@then('the user should be redirected to the dashboard')
def step_verify_dashboard_redirect(context):
    """Verify user is redirected to dashboard."""
    WebDriverWait(context.driver, 10).until(
        EC.url_contains('/dashboard')
    )
    assert '/dashboard' in context.driver.current_url, \
        f"Expected URL to contain '/dashboard', but got {context.driver.current_url}"


@then('the user should see their profile information')
def step_verify_profile_information(context):
    """Verify profile information is displayed."""
    profile_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.profile-info'))
    )
    assert profile_element.is_displayed(), "Profile information is not displayed"


@then('the user should see an error message "{expected_message}"')
def step_verify_error_message(context, expected_message):
    """Verify error message is displayed."""
    error_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.error-message'))
    )
    actual_message = error_element.text
    assert expected_message in actual_message, \
        f"Expected error message '{expected_message}', but got '{actual_message}'"


@then('the user should remain on the login page')
def step_verify_on_login_page(context):
    """Verify user remains on login page."""
    assert '/login' in context.driver.current_url, \
        f"Expected to remain on login page, but current URL is {context.driver.current_url}"


@then('the user should see validation errors')
def step_verify_validation_errors(context):
    """Verify validation errors are displayed."""
    validation_errors = context.driver.find_elements(By.CSS_SELECTOR, '.validation-error')
    assert len(validation_errors) > 0, "No validation errors found"


@then('the login button should be disabled')
def step_verify_login_button_disabled(context):
    """Verify login button is disabled."""
    login_button = context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    assert not login_button.is_enabled(), "Login button should be disabled"


@then('the user should have "{role}" permissions')
def step_verify_user_role(context, role):
    """Verify user has the expected role/permissions."""
    # This would typically check role-specific elements or API calls
    role_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f'[data-role="{role}"]'))
    )
    assert role_element.is_displayed(), f"User does not have {role} role"
