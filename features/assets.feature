Feature: Asset Management
  As a user of the EM2M application
  I want to manage assets
  So that I can track and organize my resources

  Background:
    Given the user is logged in
    And the user is on the assets page

  @smoke @assets
  Scenario: View asset list
    When the user navigates to the assets page
    Then the user should see a list of assets
    And each asset should display its basic information

  @assets @create
  Scenario: Create a new asset
    When the user clicks the "Create Asset" button
    And the user fills in the asset details
      | Field       | Value           |
      | Name        | Test Asset      |
      | Type        | Equipment       |
      | Description | Test Description|
      | Status      | Active          |
    And the user clicks the "Save" button
    Then the asset should be created successfully
    And the user should see a success message
    And the new asset should appear in the asset list

  @assets @edit
  Scenario: Edit an existing asset
    Given an asset exists with name "Test Asset"
    When the user clicks on the asset
    And the user clicks the "Edit" button
    And the user updates the asset name to "Updated Asset"
    And the user clicks the "Save" button
    Then the asset should be updated successfully
    And the updated information should be displayed

  @assets @delete
  Scenario: Delete an asset
    Given an asset exists with name "Test Asset"
    When the user clicks on the asset
    And the user clicks the "Delete" button
    And the user confirms the deletion
    Then the asset should be deleted successfully
    And the asset should not appear in the asset list

  @assets @search
  Scenario: Search for assets
    Given multiple assets exist in the system
    When the user enters "Equipment" in the search field
    Then only assets matching "Equipment" should be displayed
    And the count should match the filtered results
