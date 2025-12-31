Feature: Asset Management
  As a user of the EM2M application
  I want to manage assets
  So that I can track and organize my resources

  Background:
    Given the user is logged in with valid credentials

  @smoke @assets
  Scenario: Navigate to assets page
    When the user navigates to the assets or dashboard page
    Then the user should be on a valid page
