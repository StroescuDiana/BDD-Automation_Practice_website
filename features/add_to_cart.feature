Feature: Check that add to cart functionality is working properly

  Background:
    Given I am on Automation Practice Website's home page

    @Test_case_22
    Scenario: Add to cart from recommended items
      When I scroll to bottom of page and verify 'RECOMMENDED ITEMS' are visible
      When I click on 'Add To Cart' on recommended product
      When I click on 'View Cart'
      Then I verify that product is displayed in cart page
