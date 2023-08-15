from selenium.webdriver.common.by import By


class HomePageObjects:
    WEB_BODY = (By.CSS_SELECTOR, "body")
    EXPECTED_TEXT = "SUBSCRIPTION"
    ACTUAL_TEXT = (By.XPATH, "//div[@class='single-widget']//h2[contains(text(), 'Subscription')]")
    SUBSCRIBE_INPUT_FIELD = (By.ID, "susbscribe_email")
    ARROW_BTN = (By.ID, "subscribe")
    SUCCESS_MSG = (By.XPATH, '//div[@class="alert-success alert"][contains(text(), "You have been successfully subscribed!")]')
    RECOMMENDED_ITEMS = (By.XPATH, '//h2[@class="title text-center"][contains(text(), "recommended items")]')
    VIEW_CART_BTN = (By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
    CAROUSEL_RECOMMENDED_PRODUCTS = (By.XPATH, '//div[@id="recommended-item-carousel"]//div[@class="item active"]//div[@class="col-sm-4"]')
