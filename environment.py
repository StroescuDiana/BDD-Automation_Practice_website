from pages.home_page import HomePage
from pages.shopping_cart_page import ShoppingCartPage
from utils.webdriver import WebDriver


def before_all(context):
    context.webdriver = WebDriver()
    context.home_page = HomePage()
    context.shopping_cart_page = ShoppingCartPage()


def after_all(context):
    context.webdriver.quit()