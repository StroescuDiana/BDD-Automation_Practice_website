Feature: Check that subscription functionality is working properly

  Background:
    Given I am on the home page of Automation Practice Website

  @Test_case_10
  Scenario: Verify Subscription on the home page
    When I scroll down to the footer
    When I verify that the "SUBSCRIPTION" text is visible
    When I enter an email address in the input and click the arrow button
    Then I should see the success message "You have been successfully subscribed!"