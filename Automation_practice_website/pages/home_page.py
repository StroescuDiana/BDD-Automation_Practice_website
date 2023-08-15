from pages.base_page import BasePage
from utils.webdriver import WebDriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):

    WEB_BODY = (By.CSS_SELECTOR, "body")
    EXPECTED_TEXT = "SUBSCRIPTION"
    ACTUAL_TEXT = (By.XPATH, "//div[@class='single-widget']//h2[contains(text(), 'Subscription')]")
    SUBSCRIBE_INPUT_FIELD = (By.ID, "susbscribe_email")
    ARROW_BTN = (By.ID, "subscribe")
    SUCCESS_MSG = (By.XPATH, "//div[contains(text(), 'You have been successfully subscribed!')]")

    def load_home_page(self):
        super().driver.get('http://automationexercise.com')
        super().driver.implicitly_wait(10)

    def home_page_is_visible(self):
        is_home_page_visible = super().driver.execute_script("return document.readyState === 'complete';")
        assert is_home_page_visible, "The page is not visible or still loading."

    def scroll_to_footer(self):
        super().find(self.WEB_BODY).send_keys(Keys.CONTROL + Keys.END)

    def verify_text(self):
        actual_text = super().find(self.ACTUAL_TEXT).text
        assert self.EXPECTED_TEXT == actual_text, f"Actual text {actual_text} is different from {self.EXPECTED_TEXT}"

    def subscribe(self, email):
        super().find(self.SUBSCRIBE_INPUT_FIELD).send_keys(email)
        super().find(self.ARROW_BTN).click()

    def verify_success_message(self):
        try:
            success_message = self.wait_for_visibility_of(self.SUCCESS_MSG)
            assert success_message.is_displayed(), "Success message is not visible"

        except AssertionError:
            print("Success message is not visible")
