from behave import *


@given("I am on Automation Practice Website's home page")
def step_impl(context):
    context.home_page.load_home_page()
    context.home_page.visibility_of_home_page()


@when("I scroll to bottom of page and verify 'RECOMMENDED ITEMS' are visible")
def step_impl(context):
    context.home_page.scroll_to_footer()
    assert context.home_page.check_recommended_items_visibility(), "Recommended items section is not visible"


@when("I click on 'Add To Cart' on recommended product")
def step_impl(context):
    context.product_added = context.home_page.add_to_cart_recommended_product()

@when("I click on 'View Cart'")
def step_impl(context):
    context.home_page.click_view_cart()


@then("I verify that product is displayed in cart page")
def step_impl(context):
    product_in_cart = context.shopping_cart_page.get_displayed_product_name()
    assert context.product_added == product_in_cart, "The added product is different to cart product."