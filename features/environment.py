"""
Behave environment configuration file.
This file contains hooks that run before/after scenarios, features, and test runs.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os


def before_all(context):
    """
    Runs once before all tests.
    Setup global configurations here.
    """
    # Set base URL from environment variable or use default
    context.base_url = os.getenv('BASE_URL', 'https://elasticm2m-dev.app.em2m.net')

    # Set default timeout
    context.default_timeout = 10

    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    print("Test suite initialization complete")


def before_feature(context, feature):
    """
    Runs before each feature file.
    """
    print(f"\n{'='*80}")
    print(f"Starting Feature: {feature.name}")
    print(f"{'='*80}")


def before_scenario(context, scenario):
    """
    Runs before each scenario.
    Initialize browser here.
    """
    print(f"\nStarting Scenario: {scenario.name}")

    # Setup Chrome options
    chrome_options = Options()

    # Uncomment for headless mode
    # chrome_options.add_argument('--headless')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')

    # Initialize WebDriver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(context.default_timeout)


def after_scenario(context, scenario):
    """
    Runs after each scenario.
    Cleanup and screenshot capture on failure.
    """
    # Take screenshot on failure
    if scenario.status == 'failed':
        screenshot_dir = 'reports/screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_name = f"{scenario.name.replace(' ', '_')}_{scenario.line}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    # Close browser
    if hasattr(context, 'driver'):
        context.driver.quit()

    print(f"Scenario '{scenario.name}' completed with status: {scenario.status}")


def after_feature(context, feature):
    """
    Runs after each feature file.
    """
    print(f"\n{'='*80}")
    print(f"Completed Feature: {feature.name}")
    print(f"{'='*80}\n")


def after_all(context):
    """
    Runs once after all tests.
    Final cleanup here.
    """
    print("\nTest suite execution complete")
