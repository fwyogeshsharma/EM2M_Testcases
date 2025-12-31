"""
Page Object Model for Login Page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object."""

    # Locators (Updated based on actual application)
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.form-login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message, .alert-danger, .mat-error")
    VALIDATION_ERROR = (By.CSS_SELECTOR, ".validation-error, .mat-error")

    def __init__(self, driver):
        """Initialize the login page."""
        super().__init__(driver)
        self.base_url = "https://elasticm2m-dev.app.em2m.net"

    def navigate_to_login(self):
        """Navigate to the login page."""
        login_url = f"{self.base_url}/login"
        self.navigate_to(login_url)

    def enter_username(self, username):
        """
        Enter username.

        Args:
            username: Username to enter
        """
        self.enter_text(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Enter password.

        Args:
            password: Password to enter
        """
        self.enter_text(*self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button."""
        self.click(*self.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Perform login with username and password.

        Args:
            username: Username
            password: Password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """
        Get the error message text.

        Returns:
            Error message text
        """
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_message_displayed(self):
        """
        Check if error message is displayed.

        Returns:
            Boolean
        """
        return self.is_element_visible(*self.ERROR_MESSAGE)

    def is_validation_error_displayed(self):
        """
        Check if validation error is displayed.

        Returns:
            Boolean
        """
        return self.is_element_visible(*self.VALIDATION_ERROR)

    def is_login_button_enabled(self):
        """
        Check if login button is enabled.

        Returns:
            Boolean
        """
        button = self.find_element(*self.LOGIN_BUTTON)
        return button.is_enabled()
