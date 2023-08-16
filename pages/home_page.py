import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from objects_path.home_page_objects import HomePageObjects
from pages.base_page import BasePage


class HomePage(BasePage, HomePageObjects):

    def load_home_page(self):
        super().driver.get('http://automationexercise.com')
        super().driver.implicitly_wait(10)

    def visibility_of_home_page(self):
        return super().driver.execute_script("return document.readyState === 'complete';")

    def scroll_to_footer(self):
        super().find(super().WEB_BODY).send_keys(Keys.CONTROL + Keys.END)

    def visibility_of_SUBSCRIPTION_text(self):
        return super().find(super().ACTUAL_TEXT).is_displayed()

    def subscribe(self, email):
        super().find(super().SUBSCRIBE_INPUT_FIELD).send_keys(email)
        super().find(super().ARROW_BTN).click()

    def visibility_of_success_message(self):
        super().wait_for_visibility_of(super().SUCCESS_MSG)
        success_message = super().find(super().SUCCESS_MSG)
        return success_message.is_displayed()


    def check_recommended_items_visibility(self):
        try:
            return super().find(super().RECOMMENDED_ITEMS).is_displayed()
        except:
            return False

    def add_to_cart_recommended_product(self):
        id_elements = super().find_elements(super().CAROUSEL_RECOMMENDED_PRODUCTS)

        id_list = []

        for element in id_elements:
            anchor_element = element.find_element(By.CSS_SELECTOR, 'a[data-product-id]')
            attribute_value = anchor_element.get_attribute("data-product-id")
            integer_value = int(attribute_value)
            id_list.append(integer_value)

        min_id = min(id_list)
        max_id = max(id_list)
        random_id = random.randint(min_id, max_id)

        product_name = super().driver.find_element(By.XPATH, f"//div[@class='item active']//a[@data-product-id='{random_id}']/preceding-sibling::p").text
        super().driver.find_element(By.XPATH, f"//div[@class='item active']/div/div/div/div/a[@data-product-id='{random_id}']").click()  # clicks add to cart button
        return product_name

    def click_view_cart(self):
        super().find(super().VIEW_CART_BTN).click()