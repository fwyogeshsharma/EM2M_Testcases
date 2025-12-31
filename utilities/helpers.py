"""
Helper utilities for test automation.
"""

import os
import json
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHelpers:
    """Collection of helper methods for tests."""

    @staticmethod
    def take_screenshot(driver, name):
        """
        Take a screenshot and save it with timestamp.

        Args:
            driver: WebDriver instance
            name: Base name for the screenshot

        Returns:
            Path to saved screenshot
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "reports/screenshots"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)

        driver.save_screenshot(filepath)
        return filepath

    @staticmethod
    def wait_for_page_load(driver, timeout=30):
        """
        Wait for page to load completely.

        Args:
            driver: WebDriver instance
            timeout: Maximum wait time in seconds
        """
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @staticmethod
    def read_test_data(filename):
        """
        Read test data from JSON file.

        Args:
            filename: Name of the JSON file in test_data directory

        Returns:
            Dictionary of test data
        """
        filepath = os.path.join("test_data", filename)
        with open(filepath, 'r') as file:
            return json.load(file)

    @staticmethod
    def generate_timestamp():
        """
        Generate timestamp string.

        Returns:
            Timestamp string
        """
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def generate_unique_name(base_name):
        """
        Generate unique name with timestamp.

        Args:
            base_name: Base name to append timestamp to

        Returns:
            Unique name string
        """
        return f"{base_name}_{TestHelpers.generate_timestamp()}"
