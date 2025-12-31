"""
Page Object Model for Assets Page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AssetsPage(BasePage):
    """Assets page object."""

    # Locators (update these based on your actual application)
    ASSETS_LIST = (By.CSS_SELECTOR, ".asset-list .asset-item")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Create')]")
    EDIT_BUTTON = (By.XPATH, "//button[contains(text(),'Edit')]")
    DELETE_BUTTON = (By.XPATH, "//button[contains(text(),'Delete')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Save')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(text(),'Confirm')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='Search']")
    ASSET_NAME_INPUT = (By.ID, "assetName")
    ASSET_TYPE_INPUT = (By.ID, "assetType")
    ASSET_DESCRIPTION_INPUT = (By.ID, "assetDescription")
    ASSET_STATUS_SELECT = (By.ID, "assetStatus")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message, .alert-success")
    RESULTS_COUNT = (By.CSS_SELECTOR, ".results-count")

    def __init__(self, driver):
        """Initialize the assets page."""
        super().__init__(driver)
        self.base_url = "https://elasticm2m-dev.app.em2m.net"

    def navigate_to_assets(self):
        """Navigate to the assets page."""
        # Update this URL based on your application structure
        assets_url = f"{self.base_url}/assets"
        self.navigate_to(assets_url)

    def get_all_assets(self):
        """
        Get all asset elements from the list.

        Returns:
            List of WebElements
        """
        return self.find_elements(*self.ASSETS_LIST)

    def click_create_button(self):
        """Click the create asset button."""
        self.click(*self.CREATE_BUTTON)

    def click_edit_button(self):
        """Click the edit button."""
        self.click(*self.EDIT_BUTTON)

    def click_delete_button(self):
        """Click the delete button."""
        self.click(*self.DELETE_BUTTON)

    def click_save_button(self):
        """Click the save button."""
        self.click(*self.SAVE_BUTTON)

    def confirm_deletion(self):
        """Confirm deletion in the confirmation dialog."""
        self.click(*self.CONFIRM_DELETE_BUTTON)

    def click_button_by_text(self, button_text):
        """
        Click a button by its text.

        Args:
            button_text: Text of the button to click
        """
        button_locator = (By.XPATH, f"//button[contains(text(),'{button_text}')]")
        self.click(*button_locator)

    def fill_field(self, field_name, value):
        """
        Fill a form field based on field name.

        Args:
            field_name: Name of the field
            value: Value to enter
        """
        field_mapping = {
            'Name': self.ASSET_NAME_INPUT,
            'Type': self.ASSET_TYPE_INPUT,
            'Description': self.ASSET_DESCRIPTION_INPUT,
            'Status': self.ASSET_STATUS_SELECT
        }

        if field_name in field_mapping:
            self.enter_text(*field_mapping[field_name], value)

    def click_asset(self, asset_name):
        """
        Click on an asset by name.

        Args:
            asset_name: Name of the asset to click
        """
        asset_locator = (By.XPATH, f"//div[contains(@class,'asset-item')]//span[contains(text(),'{asset_name}')]")
        self.click(*asset_locator)

    def update_asset_name(self, new_name):
        """
        Update the asset name.

        Args:
            new_name: New name for the asset
        """
        self.enter_text(*self.ASSET_NAME_INPUT, new_name)

    def search_for(self, search_term):
        """
        Search for assets using the search field.

        Args:
            search_term: Term to search for
        """
        self.enter_text(*self.SEARCH_INPUT, search_term)

    def get_displayed_asset_name(self):
        """
        Get the currently displayed asset name.

        Returns:
            Asset name text
        """
        return self.get_text(*self.ASSET_NAME_INPUT)

    def get_results_count(self):
        """
        Get the count of search results.

        Returns:
            Integer count
        """
        count_text = self.get_text(*self.RESULTS_COUNT)
        # Extract number from text like "10 results"
        return int(''.join(filter(str.isdigit, count_text)))

    def is_success_message_displayed(self):
        """
        Check if success message is displayed.

        Returns:
            Boolean
        """
        return self.is_element_visible(*self.SUCCESS_MESSAGE)
