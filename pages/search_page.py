"""
Page Object Model for Search functionality.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class SearchPage(BasePage):
    """Search page object."""

    # Locators (Updated based on actual application)
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'search') or contains(@aria-label, 'search')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-input")
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, ".mat-mdc-autocomplete-panel, .mat-autocomplete-panel, .cdk-overlay-pane")
    DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "mat-option[role='option']")

    def __init__(self, driver):
        """Initialize the search page."""
        super().__init__(driver)

    def click_search_button(self):
        """Click the search button in the navbar (not the burger menu)."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        # Wait for the page to be ready
        time.sleep(1)

        # Store visible inputs BEFORE clicking
        inputs_before = self.driver.find_elements(By.TAG_NAME, "input")
        visible_inputs_before = [inp for inp in inputs_before if inp.is_displayed()]
        print(f"Visible inputs BEFORE clicking search button: {len(visible_inputs_before)}")

        # Find the search button (the one with text 'search')
        all_buttons = self.driver.find_elements(By.TAG_NAME, "button")
        search_button = None

        for btn in all_buttons:
            if btn.is_displayed() and 'search' in btn.text.strip().lower():
                search_button = btn
                print(f"Found search button with text: '{btn.text}'")
                break

        if not search_button:
            raise Exception("Could not find search button on navbar")

        # Use JavaScript click to avoid any overlay issues
        self.driver.execute_script("arguments[0].click();", search_button)
        print("Clicked search button")

        # Wait for NEW input to appear
        time.sleep(2)

        # Find the NEW input that appeared
        inputs_after = self.driver.find_elements(By.TAG_NAME, "input")
        visible_inputs_after = [inp for inp in inputs_after if inp.is_displayed()]
        print(f"Visible inputs AFTER clicking search button: {len(visible_inputs_after)}")

        # Store the new input for later use
        new_inputs = [inp for inp in visible_inputs_after if inp not in visible_inputs_before]
        if new_inputs:
            self.current_search_input = new_inputs[0]
            print(f"Found NEW search input with class: {self.current_search_input.get_attribute('class')}")
        else:
            # Fallback: use the last visible input
            self.current_search_input = visible_inputs_after[-1] if visible_inputs_after else None
            print("Using last visible input as search input")

    def enter_search_term(self, search_term):
        """
        Enter text in the search input field that appeared after clicking search button.

        Args:
            search_term: Text to search for
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        # Use the input that was stored when we clicked the search button
        if not hasattr(self, 'current_search_input') or self.current_search_input is None:
            raise Exception("Search input not found. Make sure to click search button first!")

        search_input = self.current_search_input
        print(f"Typing '{search_term}' into search input with class: {search_input.get_attribute('class')}")

        # Focus the input
        self.driver.execute_script("arguments[0].focus();", search_input)
        time.sleep(0.3)

        # Clear any existing value
        self.driver.execute_script("arguments[0].value = '';", search_input)

        # Type character by character to trigger autocomplete
        for char in search_term:
            search_input.send_keys(char)
            time.sleep(0.1)

        # Trigger input and keyup events for Angular
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", search_input)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('keyup', { bubbles: true }));", search_input)

        print(f"Typed '{search_term}' successfully")

        # Wait for autocomplete to trigger
        time.sleep(3)

    def wait_for_dropdown(self, timeout=15):
        """
        Wait for the search dropdown to appear.

        Args:
            timeout: Maximum wait time in seconds
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        # Wait for mat-option elements to appear
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "mat-option[role='option']"))
            )
            print("Dropdown with mat-option elements found")
            time.sleep(0.5)
        except:
            print("Warning: Dropdown not found, continuing anyway...")
            time.sleep(1)

    def is_dropdown_visible(self):
        """
        Check if the search dropdown is visible.

        Returns:
            Boolean
        """
        return self.is_element_visible(*self.SEARCH_DROPDOWN, timeout=5)

    def get_dropdown_options(self):
        """
        Get all options from the search dropdown.

        Returns:
            List of WebElements
        """
        # Get all mat-option elements with role='option'
        options = self.driver.find_elements(By.CSS_SELECTOR, "mat-option[role='option']")
        visible_options = [opt for opt in options if opt.is_displayed()]
        print(f"Found {len(visible_options)} visible dropdown options")
        return visible_options

    def get_dropdown_option_texts(self):
        """
        Get text of all dropdown options.

        Returns:
            List of strings
        """
        options = self.get_dropdown_options()
        return [option.text for option in options]

    def click_exact_match(self, text):
        """
        Click on an exact match from the dropdown.

        Args:
            text: Exact text to match and click
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

        # Wait for mat-option elements to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option[role='option']"))
        )

        options = self.get_dropdown_options()
        print(f"Searching for exact match '{text}' in {len(options)} options")

        for option in options:
            option_text = option.text.strip()
            print(f"  Option text: '{option_text}'")

            # Check if this option contains the exact text
            if option_text == text.strip():
                print(f"Found exact match: '{option_text}', clicking...")

                # Click using JavaScript to avoid interception
                self.driver.execute_script("arguments[0].click();", option)
                time.sleep(1)
                return

        raise Exception(f"Exact match '{text}' not found in dropdown. Available options: {[opt.text.strip() for opt in options]}")

    def click_partial_match(self, text):
        """
        Click on a partial match from the dropdown.

        Args:
            text: Text to partially match and click
        """
        options = self.get_dropdown_options()
        for option in options:
            if text.lower() in option.text.lower():
                option.click()
                return
        raise Exception(f"Partial match containing '{text}' not found in dropdown")

    def is_text_in_dropdown(self, text):
        """
        Check if specific text appears in dropdown options.

        Args:
            text: Text to search for

        Returns:
            Boolean
        """
        option_texts = self.get_dropdown_option_texts()
        return any(text.lower() in option.lower() for option in option_texts)

    def search_and_select(self, search_term):
        """
        Complete search flow: click button, enter text, select exact match.

        Args:
            search_term: Term to search for and select
        """
        self.click_search_button()
        self.enter_search_term(search_term)
        self.wait_for_dropdown()
        self.click_exact_match(search_term)
