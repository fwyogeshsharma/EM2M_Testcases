"""
Base Page class containing common methods for all pages.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        """Initialize the base page."""
        self.driver = driver
        self.timeout = 10

    def find_element(self, by, value):
        """
        Find an element with explicit wait.

        Args:
            by: Locator strategy (By.ID, By.CSS_SELECTOR, etc.)
            value: Locator value

        Returns:
            WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_elements(self, by, value):
        """
        Find multiple elements.

        Args:
            by: Locator strategy
            value: Locator value

        Returns:
            List of WebElements
        """
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        """
        Click an element after waiting for it to be clickable.

        Args:
            by: Locator strategy
            value: Locator value
        """
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def enter_text(self, by, value, text):
        """
        Enter text into an input field.

        Args:
            by: Locator strategy
            value: Locator value
            text: Text to enter
        """
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        """
        Get text from an element.

        Args:
            by: Locator strategy
            value: Locator value

        Returns:
            Element text
        """
        element = self.find_element(by, value)
        return element.text

    def is_element_visible(self, by, value, timeout=None):
        """
        Check if an element is visible.

        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional custom timeout

        Returns:
            Boolean
        """
        try:
            wait_timeout = timeout if timeout else self.timeout
            WebDriverWait(self.driver, wait_timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, url_part, timeout=None):
        """
        Wait for URL to contain a specific part.

        Args:
            url_part: Part of the URL to wait for
            timeout: Optional custom timeout
        """
        wait_timeout = timeout if timeout else self.timeout
        WebDriverWait(self.driver, wait_timeout).until(
            EC.url_contains(url_part)
        )

    def wait_for_element_to_disappear(self, by, value, timeout=None):
        """
        Wait for an element to disappear.

        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional custom timeout
        """
        wait_timeout = timeout if timeout else self.timeout
        WebDriverWait(self.driver, wait_timeout).until(
            EC.invisibility_of_element_located((by, value))
        )

    def scroll_to_element(self, element):
        """
        Scroll to an element.

        Args:
            element: WebElement to scroll to
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self):
        """Get the current URL."""
        return self.driver.current_url

    def get_page_title(self):
        """Get the page title."""
        return self.driver.title

    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()

    def navigate_to(self, url):
        """
        Navigate to a specific URL.

        Args:
            url: URL to navigate to
        """
        self.driver.get(url)
