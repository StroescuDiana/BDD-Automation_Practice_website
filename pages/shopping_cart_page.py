from objects_path.shopping_cart_objects import ShoppingCartObjects
from pages.base_page import BasePage


class ShoppingCartPage(BasePage, ShoppingCartObjects):

    def get_displayed_product_name(self):
        return super().find(super().PRODUCT_NAME_CART).text