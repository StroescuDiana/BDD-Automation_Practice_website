from behave import given, when, then

from pages.home_page import HomePage


@given("I am on the home page of Automation Practice Website")
def step_impl(context):
    context.page = HomePage()
    context.page.load_home_page()


@when("I scroll down to the footer")
def step_impl(context):
    context.page.scroll_to_footer()


@when('I verify that the "SUBSCRIPTION" text is visible')
def step_impl(context):
    context.page.verify_text()


@when('I enter an email address in the input and click the arrow button')
def step_impl(context):
    context.page.subscribe(context.config.userdata['email'])


@then('I should see the success message "You have been successfully subscribed!"')
def step_impl(context):
    context.page.verify_success_message()