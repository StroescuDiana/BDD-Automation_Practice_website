from selenium.webdriver.common.by import By


class ShoppingCartObjects:
    PRODUCT_NAME_CART = (By.XPATH, '//td[@class="cart_description"]/h4/a')