Feature: Add all the content form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed

  @smoke
  Scenario: Test transition is ok
    Given Go to form page
    Then The form should be displayed
    When Go to home page
    Then The home page be displayed

    # TODO implementarea celorlate feature files - tot ce trebuie sa folosim este din pagini