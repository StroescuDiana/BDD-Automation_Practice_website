from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class BasePage(WebDriver):

    def find(self, locator: tuple):
        return super().driver.find_element(*locator)

    def wait_for_visibility_of(self, locator: tuple):
        WebDriverWait(super().driver, 10).until(EC.visibility_of_element_located(locator))

