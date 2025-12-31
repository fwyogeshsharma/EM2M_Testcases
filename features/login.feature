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
    Then the user should see an error message "Incorrect username or password"
    And the user should remain on the login page

  @login @negative
  Scenario: Login with empty credentials
    When the user leaves username and password empty
    And the user clicks the login button
    Then the user should see an error message "Invalid username or password"
    And the user should remain on the login page

  @login
  Scenario: Login with valid user role
    When the user enters valid username and password
    And the user clicks the login button
    Then the user should be redirected to the dashboard
