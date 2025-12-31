Feature: User Login
  As a user of the EM2M application
  I want to be able to log in to the system
  So that I can access my account and manage assets

  Background:
    Given the user is on the login page

  @smoke @login
  Scenario: Successful login with valid credentials
    When the user enters valid username and password
    And the user clicks the login button
    Then the user should be redirected to the dashboard
    And the user should see their profile information

  @login @negative
  Scenario: Login with invalid credentials
    When the user enters invalid username and password
    And the user clicks the login button
    Then the user should see an error message "Invalid credentials"
    And the user should remain on the login page

  @login @negative
  Scenario: Login with empty credentials
    When the user leaves username and password empty
    And the user clicks the login button
    Then the user should see validation errors
    And the login button should be disabled

  @login
  Scenario Outline: Login with different user roles
    When the user enters "<username>" and "<password>"
    And the user clicks the login button
    Then the user should be redirected to the dashboard
    And the user should have "<role>" permissions

    Examples:
      | username      | password    | role      |
      | admin@em2m.net | admin123   | admin     |
      | user@em2m.net  | user123    | user      |
      | viewer@em2m.net| viewer123  | viewer    |
