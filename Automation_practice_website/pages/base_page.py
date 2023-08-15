from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class BasePage(WebDriver):

    def find(self, locator: tuple):
        return super().driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return super().driver.find_elements(*locator)

    def wait_for_visibility_of(self, locator: tuple):
        wait = WebDriverWait(super().driver, 10)
        wait.until(EC.visibility_of_element_located(locator))