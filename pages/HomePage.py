import time

from pages.AdminPage import AdminPage
from pages.BasePage import BasePage
from pages.PimPage import PimPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def go_to_admin_page(self):
        self.click("admin_link_XPATH")
        return AdminPage(self.driver)

    def go_to_PIM_page(self):
        self.click("pim_link_XPATH")
        return PimPage(self.driver)
