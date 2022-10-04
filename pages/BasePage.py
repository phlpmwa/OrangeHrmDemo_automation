from selenium.webdriver.common.by import By

from utilities.configreader import read_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):

        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=By.XPATH, value=read_config("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=By.ID, value=read_config("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(by=By.CSS_SELECTOR, value=read_config("locators", locator)).click()

    def type(self, locator, value):
        if str(locator).endswith("_CSS"):
            self.driver.find_element(by=By.CSS_SELECTOR, value=read_config("locators", locator)).send_keys(value)


