from behave import given, when, then


@given("I am on the home page of Automation Practice Website")
def step_impl(context):
    context.home_page.load_home_page()
    assert context.home_page.visibility_of_home_page(), "The page is not visible or still loading."

@when("I scroll down to the footer")
def step_impl(context):
    context.home_page.scroll_to_footer()

@when('I verify that the "SUBSCRIPTION" text is visible')
def step_impl(context):
    assert context.home_page.visibility_of_SUBSCRIPTION_text(), "SUBSCRIPTION text is not visible."

@when('I enter an email address in the input and click the arrow button')
def step_impl(context):
    context.home_page.subscribe(context.config.userdata["email"])

@then('I should see the success message "You have been successfully subscribed!"')
def step_impl(context):
    assert context.home_page.visibility_of_success_message(), "Success message is not visible"