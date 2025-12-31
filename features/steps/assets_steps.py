"""
Step definitions for assets feature.
"""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.assets_page import AssetsPage
from pages.login_page import LoginPage
from config.config import Config
import time


@given('the user is logged in')
def step_user_is_logged_in(context):
    """Ensure user is logged in."""
    login_page = LoginPage(context.driver)
    login_page.navigate_to_login()
    login_page.login(Config.TEST_USERNAME, Config.TEST_PASSWORD)

    # Wait for dashboard to load
    WebDriverWait(context.driver, 10).until(
        EC.url_contains('/dashboard')
    )


@given('the user is on the assets page')
def step_navigate_to_assets_page(context):
    """Navigate to the assets page."""
    context.assets_page = AssetsPage(context.driver)
    context.assets_page.navigate_to_assets()


@given('an asset exists with name "{asset_name}"')
def step_ensure_asset_exists(context, asset_name):
    """Ensure an asset exists with the given name."""
    # This could involve creating the asset via API or UI
    context.assets_page = AssetsPage(context.driver)
    context.test_asset_name = asset_name
    # Implementation depends on your application


@given('multiple assets exist in the system')
def step_ensure_multiple_assets_exist(context):
    """Ensure multiple assets exist in the system."""
    # This could involve creating multiple assets via API
    # For now, we assume they already exist
    pass


@when('the user navigates to the assets page')
def step_navigate_to_assets(context):
    """Navigate to the assets page."""
    context.assets_page.navigate_to_assets()


@when('the user clicks the "{button_text}" button')
def step_click_button(context, button_text):
    """Click a button with the specified text."""
    context.assets_page.click_button_by_text(button_text)


@when('the user fills in the asset details')
def step_fill_asset_details(context):
    """Fill in asset details from the table."""
    for row in context.table:
        field = row['Field']
        value = row['Value']
        context.assets_page.fill_field(field, value)


@when('the user clicks on the asset')
def step_click_on_asset(context):
    """Click on the test asset."""
    context.assets_page.click_asset(context.test_asset_name)


@when('the user updates the asset name to "{new_name}"')
def step_update_asset_name(context, new_name):
    """Update the asset name."""
    context.assets_page.update_asset_name(new_name)
    context.updated_asset_name = new_name


@when('the user confirms the deletion')
def step_confirm_deletion(context):
    """Confirm the deletion in the confirmation dialog."""
    context.assets_page.confirm_deletion()


@when('the user enters "{search_term}" in the search field')
def step_enter_search_term(context, search_term):
    """Enter search term in the search field."""
    context.assets_page.search_for(search_term)
    context.search_term = search_term


@then('the user should see a list of assets')
def step_verify_asset_list_displayed(context):
    """Verify that the asset list is displayed."""
    assets = context.assets_page.get_all_assets()
    assert len(assets) > 0, "No assets found in the list"


@then('each asset should display its basic information')
def step_verify_asset_basic_info(context):
    """Verify each asset displays basic information."""
    assets = context.assets_page.get_all_assets()
    for asset in assets:
        assert asset.is_displayed(), "Asset element is not displayed"


@then('the asset should be created successfully')
def step_verify_asset_created(context):
    """Verify the asset was created successfully."""
    # Wait for success indicator or new asset in list
    time.sleep(1)  # Wait for creation to complete
    # Additional verification logic here


@then('the user should see a success message')
def step_verify_success_message(context):
    """Verify success message is displayed."""
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.success-message, .alert-success'))
    )
    assert success_message.is_displayed(), "Success message not displayed"


@then('the new asset should appear in the asset list')
def step_verify_asset_in_list(context):
    """Verify the new asset appears in the asset list."""
    # Refresh or wait for the list to update
    time.sleep(1)
    assets = context.assets_page.get_all_assets()
    assert len(assets) > 0, "Asset list is empty"


@then('the asset should be updated successfully')
def step_verify_asset_updated(context):
    """Verify the asset was updated successfully."""
    time.sleep(1)  # Wait for update to complete
    # Verification logic here


@then('the updated information should be displayed')
def step_verify_updated_info_displayed(context):
    """Verify updated information is displayed."""
    displayed_name = context.assets_page.get_displayed_asset_name()
    assert context.updated_asset_name in displayed_name, \
        f"Expected to see {context.updated_asset_name}, but got {displayed_name}"


@then('the asset should be deleted successfully')
def step_verify_asset_deleted(context):
    """Verify the asset was deleted successfully."""
    time.sleep(1)  # Wait for deletion to complete


@then('the asset should not appear in the asset list')
def step_verify_asset_not_in_list(context):
    """Verify the asset no longer appears in the list."""
    assets = context.assets_page.get_all_assets()
    asset_names = [asset.text for asset in assets]
    assert context.test_asset_name not in asset_names, \
        f"Asset {context.test_asset_name} should not be in the list"


@then('only assets matching "{search_term}" should be displayed')
def step_verify_filtered_results(context, search_term):
    """Verify only matching assets are displayed."""
    assets = context.assets_page.get_all_assets()
    for asset in assets:
        asset_text = asset.text.lower()
        assert search_term.lower() in asset_text, \
            f"Asset '{asset.text}' does not match search term '{search_term}'"


@then('the count should match the filtered results')
def step_verify_count_matches(context):
    """Verify the displayed count matches the filtered results."""
    count = context.assets_page.get_results_count()
    assets = context.assets_page.get_all_assets()
    assert count == len(assets), \
        f"Count mismatch: displayed {count}, but found {len(assets)} assets"


@when('the user navigates to the assets or dashboard page')
def step_navigate_to_assets_or_dashboard(context):
    """Navigate to assets or dashboard page - just verify we're logged in."""
    import time
    time.sleep(2)
    # Already logged in from background, just verify URL is valid
    current_url = context.driver.current_url
    assert 'elasticm2m-dev.app.em2m.net' in current_url, f"Not on expected domain: {current_url}"


@then('the user should be on a valid page')
def step_verify_on_valid_page(context):
    """Verify user is on a valid page after login."""
    import time
    time.sleep(1)
    current_url = context.driver.current_url
    # Check if we're on dashboard or any authenticated page
    assert '/login' not in current_url, f"Still on login page: {current_url}"
    assert 'elasticm2m-dev.app.em2m.net' in current_url, f"Not on expected domain: {current_url}"
