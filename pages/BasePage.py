from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element(by=By.XPATH, value=read_config("locators", locator)).send_keys(value)

    def elements(self, locator, index):
        global count
        if str(locator).endswith("_XPATH"):
            count = self.driver.find_elements(by=By.XPATH, value=read_config("locators", locator))[index]
        return count

    def find_elements(self, locator):
        if str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(by=By.CSS_SELECTOR, value=read_config("locators", locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(dropdown).release().perform()



