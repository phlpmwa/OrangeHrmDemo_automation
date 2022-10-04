import time

from pages.BasePage import BasePage
from pages.HomePage import HomePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self):
        self.type("username_CSS", 'Admin')
        self.type("password_CSS", 'admin123')
        self.click("login_XPATH")
        time.sleep(3)
        return HomePage(self.driver)
