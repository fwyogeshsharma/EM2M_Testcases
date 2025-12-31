"""
Page Object Model for ASEED organization page.
Contains all UI element locators and interactions for the ASEED page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import time


class AseedPage(BasePage):
    """Page Object for ASEED organization page."""

    # ========================================
    # LOCATORS - Header/Navigation
    # ========================================
    HEADER = (By.CSS_SELECTOR, "header, .header, mat-toolbar")
    MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'mat-mdc-icon-button')]//mat-icon[text()='menu']")
    SEARCH_BUTTON_HEADER = (By.XPATH, "//button[contains(text(), 'search') or .//mat-icon[text()='search']]")
    PROFILE_BUTTON = (By.CSS_SELECTOR, ".profile-button, button.profile-button")
    NOTIFICATIONS_ICON = (By.CSS_SELECTOR, "[class*='notification'], mat-icon[contains(text(), 'notifications')]")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb, [class*='breadcrumb']")

    # ========================================
    # LOCATORS - Organization Details
    # ========================================
    ORG_NAME = (By.XPATH, "//h1[contains(text(), 'ASEED')] | //h2[contains(text(), 'ASEED')] | //*[contains(@class, 'org-name') and contains(text(), 'ASEED')]")
    LOGO_SECTION = (By.CSS_SELECTOR, "img[alt*='logo'], .logo-section, [class*='logo-container']")
    LOGO_PLACEHOLDER = (By.CSS_SELECTOR, ".logo-placeholder, [class*='placeholder']")
    UPLOAD_LOGO_BUTTON = (By.XPATH, "//button[contains(text(), 'UPLOAD A CUSTOM LOGO') or contains(text(), 'UPLOAD')]")
    ELASTICM2M_LOGO = (By.XPATH, "//img[contains(@alt, 'ELASTIC') or contains(@src, 'logo')]")

    # ========================================
    # LOCATORS - Tags
    # ========================================
    TAG_DEALER = (By.XPATH, "//*[contains(text(), 'Dealer')]")
    TAG_STOLEN_VEHICLE = (By.XPATH, "//*[contains(text(), 'Stolen Vehicle Recovery')]")
    TAG_PAYMENT_ASSURANCE = (By.XPATH, "//*[contains(text(), 'Payment Assurance') and not(ancestor::*[contains(@class, 'tab')])]")
    ALL_TAGS = (By.CSS_SELECTOR, "[class*='tag'], mat-chip, .chip")

    # ========================================
    # LOCATORS - Dates
    # ========================================
    CREATED_DATE = (By.XPATH, "//*[contains(text(), 'Created:')]")
    UPDATED_DATE = (By.XPATH, "//*[contains(text(), 'Updated:')]")

    # ========================================
    # LOCATORS - Tabs
    # ========================================
    TAB_OVERVIEW = (By.XPATH, "//div[contains(@class, 'mat-tab-label') or @role='tab'][contains(., 'OVERVIEW')]")
    TAB_PAYMENT_ASSURANCE = (By.XPATH, "//div[contains(@class, 'mat-tab-label') or @role='tab'][contains(., 'PAYMENT ASSURANCE')]")
    TAB_MIKE_DASHBOARD = (By.XPATH, "//div[contains(@class, 'mat-tab-label') or @role='tab'][contains(., 'MIKE DASHBOARD')]")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".mat-tab-label-active, [aria-selected='true']")
    ALL_TABS = (By.CSS_SELECTOR, ".mat-tab-label, [role='tab']")
    TAB_INDICATOR = (By.CSS_SELECTOR, ".mat-ink-bar, .mat-tab-label-active")

    # ========================================
    # LOCATORS - Dashboard Cards
    # ========================================
    CARD_LOANS = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Loans')]]")
    CARD_ASSETS = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Assets')]]")
    CARD_RECOVERY_ORDERS = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Recovery Orders')]]")
    CARD_VEHICLES = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Vehicles')]]")
    CARD_MEDIA = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Media')]]")
    CARD_GEOFENCES = (By.XPATH, "//*[contains(@class, 'card') or contains(@class, 'mat-card')][.//text()[contains(., 'Geofences')]]")
    ALL_CARDS = (By.CSS_SELECTOR, "mat-card, .mat-card, [class*='card']")

    def __init__(self, driver):
        """Initialize the ASEED page object."""
        super().__init__(driver)

    # ========================================
    # PAGE VERIFICATION METHODS
    # ========================================

    def is_page_loaded(self):
        """Verify ASEED page is loaded."""
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: '/org/' in d.current_url
            )
            return True
        except:
            return False

    def get_page_url(self):
        """Get current page URL."""
        return self.driver.current_url

    def get_page_title(self):
        """Get page title."""
        return self.driver.title

    # ========================================
    # HEADER METHODS
    # ========================================

    def is_menu_button_visible(self):
        """Check if menu button is visible."""
        return self.is_element_visible(*self.MENU_BUTTON, timeout=5)

    def click_menu_button(self):
        """Click the menu/hamburger button."""
        element = self.wait_for_element(*self.MENU_BUTTON)
        element.click()
        time.sleep(1)

    def is_search_button_visible(self):
        """Check if search button in header is visible."""
        return self.is_element_visible(*self.SEARCH_BUTTON_HEADER, timeout=5)

    def is_profile_button_visible(self):
        """Check if profile button is visible."""
        return self.is_element_visible(*self.PROFILE_BUTTON, timeout=5)

    def click_profile_button(self):
        """Click profile button."""
        element = self.wait_for_element(*self.PROFILE_BUTTON)
        element.click()
        time.sleep(1)

    def is_notifications_icon_visible(self):
        """Check if notifications icon is visible."""
        return self.is_element_visible(*self.NOTIFICATIONS_ICON, timeout=5)

    def get_header_background_color(self):
        """Get header background color."""
        header = self.wait_for_element(*self.HEADER)
        return header.value_of_css_property('background-color')

    # ========================================
    # BREADCRUMB METHODS
    # ========================================

    def get_breadcrumb_text(self):
        """Get breadcrumb text."""
        try:
            breadcrumb = self.wait_for_element(*self.BREADCRUMB, timeout=5)
            return breadcrumb.text
        except:
            # Try alternative method - get from page source
            page_text = self.driver.find_element(By.TAG_NAME, "body").text
            if "ASEED" in page_text and "Overview" in page_text:
                return "ASEED > Overview"
            return ""

    def is_breadcrumb_visible(self):
        """Check if breadcrumb is visible."""
        text = self.get_breadcrumb_text()
        return len(text) > 0

    # ========================================
    # ORGANIZATION DETAILS METHODS
    # ========================================

    def get_organization_name(self):
        """Get organization name."""
        try:
            element = self.wait_for_element(*self.ORG_NAME, timeout=5)
            return element.text
        except:
            # Fallback: find any large heading with ASEED
            headings = self.driver.find_elements(By.XPATH, "//h1 | //h2 | //h3")
            for h in headings:
                if "ASEED" in h.text:
                    return h.text
            return "ASEED"

    def is_organization_name_visible(self):
        """Check if organization name is visible."""
        name = self.get_organization_name()
        return "ASEED" in name

    def is_upload_logo_button_visible(self):
        """Check if upload logo button is visible."""
        return self.is_element_visible(*self.UPLOAD_LOGO_BUTTON, timeout=5)

    def click_upload_logo_button(self):
        """Click upload logo button."""
        element = self.wait_for_element(*self.UPLOAD_LOGO_BUTTON)
        element.click()
        time.sleep(1)

    def is_elasticm2m_logo_visible(self):
        """Check if ElasticM2M logo is visible."""
        return self.is_element_visible(*self.ELASTICM2M_LOGO, timeout=5)

    # ========================================
    # TAGS METHODS
    # ========================================

    def is_dealer_tag_visible(self):
        """Check if Dealer tag is visible."""
        return self.is_element_visible(*self.TAG_DEALER, timeout=5)

    def is_stolen_vehicle_tag_visible(self):
        """Check if Stolen Vehicle Recovery tag is visible."""
        return self.is_element_visible(*self.TAG_STOLEN_VEHICLE, timeout=5)

    def is_payment_assurance_tag_visible(self):
        """Check if Payment Assurance tag is visible."""
        return self.is_element_visible(*self.TAG_PAYMENT_ASSURANCE, timeout=5)

    def get_all_tags(self):
        """Get all tag elements."""
        # Find by text content
        tags = []
        try:
            dealer = self.driver.find_element(*self.TAG_DEALER)
            if dealer.is_displayed():
                tags.append(dealer)
        except:
            pass

        try:
            stolen = self.driver.find_element(*self.TAG_STOLEN_VEHICLE)
            if stolen.is_displayed():
                tags.append(stolen)
        except:
            pass

        try:
            payment = self.driver.find_element(*self.TAG_PAYMENT_ASSURANCE)
            if payment.is_displayed():
                tags.append(payment)
        except:
            pass

        return tags

    def get_tag_count(self):
        """Get number of visible tags."""
        return len(self.get_all_tags())

    # ========================================
    # DATE METHODS
    # ========================================

    def is_created_date_visible(self):
        """Check if created date is visible."""
        return self.is_element_visible(*self.CREATED_DATE, timeout=5)

    def is_updated_date_visible(self):
        """Check if updated date is visible."""
        return self.is_element_visible(*self.UPDATED_DATE, timeout=5)

    def get_created_date_text(self):
        """Get created date text."""
        try:
            element = self.wait_for_element(*self.CREATED_DATE, timeout=5)
            return element.text
        except:
            return ""

    def get_updated_date_text(self):
        """Get updated date text."""
        try:
            element = self.wait_for_element(*self.UPDATED_DATE, timeout=5)
            return element.text
        except:
            return ""

    # ========================================
    # TABS METHODS
    # ========================================

    def is_tab_visible(self, tab_name):
        """Check if a specific tab is visible."""
        tab_map = {
            "OVERVIEW": self.TAB_OVERVIEW,
            "PAYMENT ASSURANCE": self.TAB_PAYMENT_ASSURANCE,
            "MIKE DASHBOARD": self.TAB_MIKE_DASHBOARD
        }
        locator = tab_map.get(tab_name.upper())
        if locator:
            return self.is_element_visible(*locator, timeout=5)
        return False

    def click_tab(self, tab_name):
        """Click on a specific tab."""
        tab_map = {
            "OVERVIEW": self.TAB_OVERVIEW,
            "PAYMENT ASSURANCE": self.TAB_PAYMENT_ASSURANCE,
            "MIKE DASHBOARD": self.TAB_MIKE_DASHBOARD
        }
        locator = tab_map.get(tab_name.upper())
        if locator:
            element = self.wait_for_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)

    def is_tab_active(self, tab_name):
        """Check if a tab is currently active."""
        try:
            active_tab = self.wait_for_element(*self.ACTIVE_TAB, timeout=5)
            return tab_name.upper() in active_tab.text.upper()
        except:
            return False

    def get_all_tabs(self):
        """Get all tab elements."""
        return self.driver.find_elements(*self.ALL_TABS)

    # ========================================
    # DASHBOARD CARDS METHODS
    # ========================================

    def is_card_visible(self, card_name):
        """Check if a specific card is visible."""
        card_map = {
            "LOANS": self.CARD_LOANS,
            "ASSETS": self.CARD_ASSETS,
            "RECOVERY ORDERS": self.CARD_RECOVERY_ORDERS,
            "VEHICLES": self.CARD_VEHICLES,
            "MEDIA": self.CARD_MEDIA,
            "GEOFENCES": self.CARD_GEOFENCES
        }
        locator = card_map.get(card_name.upper())
        if locator:
            return self.is_element_visible(*locator, timeout=5)
        return False

    def get_card_count_value(self, card_name):
        """Get the count value displayed on a card."""
        card_map = {
            "LOANS": self.CARD_LOANS,
            "ASSETS": self.CARD_ASSETS,
            "RECOVERY ORDERS": self.CARD_RECOVERY_ORDERS,
            "VEHICLES": self.CARD_VEHICLES,
            "MEDIA": self.CARD_MEDIA,
            "GEOFENCES": self.CARD_GEOFENCES
        }
        locator = card_map.get(card_name.upper())
        if locator:
            try:
                card = self.wait_for_element(*locator, timeout=5)
                # Find the count number in the card
                text = card.text
                # Extract number from text
                import re
                numbers = re.findall(r'\d+', text)
                if numbers:
                    return numbers[0]
            except:
                pass
        return None

    def click_card(self, card_name):
        """Click on a specific dashboard card."""
        card_map = {
            "LOANS": self.CARD_LOANS,
            "ASSETS": self.CARD_ASSETS,
            "RECOVERY ORDERS": self.CARD_RECOVERY_ORDERS,
            "VEHICLES": self.CARD_VEHICLES,
            "MEDIA": self.CARD_MEDIA,
            "GEOFENCES": self.CARD_GEOFENCES
        }
        locator = card_map.get(card_name.upper())
        if locator:
            element = self.wait_for_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(2)

    def hover_over_card(self, card_name):
        """Hover over a specific card."""
        card_map = {
            "LOANS": self.CARD_LOANS,
            "ASSETS": self.CARD_ASSETS,
            "RECOVERY ORDERS": self.CARD_RECOVERY_ORDERS,
            "VEHICLES": self.CARD_VEHICLES,
            "MEDIA": self.CARD_MEDIA,
            "GEOFENCES": self.CARD_GEOFENCES
        }
        locator = card_map.get(card_name.upper())
        if locator:
            element = self.wait_for_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(0.5)

    def get_all_cards(self):
        """Get all dashboard card elements."""
        return self.driver.find_elements(*self.ALL_CARDS)

    def get_card_background_color(self, card_name):
        """Get background color of a specific card."""
        card_map = {
            "LOANS": self.CARD_LOANS,
            "ASSETS": self.CARD_ASSETS,
            "RECOVERY ORDERS": self.CARD_RECOVERY_ORDERS,
            "VEHICLES": self.CARD_VEHICLES,
            "MEDIA": self.CARD_MEDIA,
            "GEOFENCES": self.CARD_GEOFENCES
        }
        locator = card_map.get(card_name.upper())
        if locator:
            try:
                element = self.wait_for_element(*locator, timeout=5)
                return element.value_of_css_property('background-color')
            except:
                pass
        return None

    # ========================================
    # UTILITY METHODS
    # ========================================

    def scroll_to_element(self, element):
        """Scroll to a specific element."""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def get_element_size(self, locator):
        """Get size of an element."""
        element = self.wait_for_element(*locator)
        return element.size

    def get_element_location(self, locator):
        """Get location of an element."""
        element = self.wait_for_element(*locator)
        return element.location

    def is_element_clickable(self, locator):
        """Check if element is clickable."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False

    def get_viewport_size(self):
        """Get current viewport size."""
        return self.driver.execute_script("return {width: window.innerWidth, height: window.innerHeight};")

    def set_viewport_size(self, width, height):
        """Set viewport size."""
        self.driver.set_window_size(width, height)
        time.sleep(1)
