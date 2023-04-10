Feature: Home page welcome message
  As a user
  I want to be welcome
  So that I know I am on the right spot

  @smoke
  Scenario: check welcome message
    When Logo is displayed
    Then I should see "Welcome to Formy"


