import time

from pages.BasePage import BasePage


class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_employee(self):
        self.click("pim_add_XPATH")
        time.sleep(20)
        self.click("pim_name_XPATH")
        self.type("pim_name_XPATH", "Hello")
        self.click("pim_save_btn_XPATH ")
