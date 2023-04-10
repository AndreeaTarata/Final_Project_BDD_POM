Feature: Add all the content form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed

  @regression
  Scenario Outline: populate multiple fields
    Given Go to form page
    When I enter first name "<first_name>"
    And I enter first name "<last_name>"
    And click submit
    Then a success message should be displayed
    Examples:
      | first_name | last_name  |
      | Andreea    | Cara       |
      | Ion        | Creanga    |
      | Ileana     | Cosanzeana |