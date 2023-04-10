Feature: Click all checkboxes
  As a user
  I want to be able to check all the checkboxes
  So I know that I have all options available

  Background:
    Given Go to checkboxes

  Scenario: click all checkboxes
    Given I am on Checkbox page
    When I click all checkboxes
    Then I want all to be enabled


  Scenario: click first checkbox
    Given I am on Checkbox page
    When I click the first checkbox
    Then I want only the first checkbox to be enabled

  Scenario: click second checkbox
    Given I am on Checkbox page
    When I click the second checkbox
    Then I want only the second checkbox to be enabled



