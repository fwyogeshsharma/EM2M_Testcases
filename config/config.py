"""
Configuration settings for test automation.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for test settings."""

    # Application URLs
    BASE_URL = os.getenv('BASE_URL', 'https://elasticm2m-dev.app.em2m.net')
    LOGIN_URL = f"{BASE_URL}/login"
    DASHBOARD_URL = f"{BASE_URL}/dashboard"
    ASSETS_URL = f"{BASE_URL}/assets"

    # Test credentials
    TEST_USERNAME = os.getenv('TEST_USERNAME', 'testuser@em2m.net')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD', 'TestPassword123')

    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin@em2m.net')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    WINDOW_SIZE = os.getenv('WINDOW_SIZE', '1920,1080')

    # Timeout settings
    DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '10'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

    # Report settings
    REPORT_DIR = os.getenv('REPORT_DIR', 'reports')
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, 'screenshots')

    # API settings (if needed)
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://elasticm2m-dev.app.em2m.net/api')
    API_TOKEN = os.getenv('API_TOKEN', '')

    @classmethod
    def get_browser_options(cls):
        """
        Get browser options based on configuration.

        Returns:
            Dictionary of browser options
        """
        return {
            'headless': cls.HEADLESS,
            'window_size': cls.WINDOW_SIZE,
            'timeout': cls.DEFAULT_TIMEOUT
        }
