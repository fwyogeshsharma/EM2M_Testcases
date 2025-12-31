Feature: Search Functionality
  As a user of the EM2M application
  I want to search for items using the search bar
  So that I can quickly find specific assets

  Background:
    Given the user is logged in with valid credentials

  @smoke @search
  Scenario: Search for ASEED and select exact match
    When the user clicks the search button in the navbar
    And the user enters "ASEED" in the search input field
    And the user waits for the dropdown to appear
    Then the user should see "ASEED" in the dropdown
    When the user clicks on the exact match "ASEED"
    Then the user should be on the ASEED details page

  @search
  Scenario: Search for item and verify results
    When the user clicks the search button in the navbar
    And the user enters "ASEED" in the search input field
    Then the dropdown should display matching results
    And the dropdown should contain "ASEED"

  @search
  Scenario Outline: Search for different items
    When the user clicks the search button in the navbar
    And the user enters "<search_term>" in the search input field
    And the user waits for the dropdown to appear
    Then the dropdown should display matching results

    Examples:
      | search_term |
      | ASEED       |
      | Asset       |
      | Equipment   |
