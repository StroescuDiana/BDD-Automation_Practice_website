Feature: Add to cart functionality

  Background:
    Given I am on Automation Practice Website's home page

    @Test_case_22
    Scenario: Verify that user can add items from the recommended section to cart
      When I scroll to bottom of page and verify 'RECOMMENDED ITEMS' are visible
      When I click on 'Add To Cart' on recommended product
      When I click on 'View Cart'
      Then I verify that product is displayed in cart page
