import time

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest


class Test_AdminPage(BaseTest):
    def test_add_admin_user(self):
        login = LoginPage(self.driver)
        login.do_login().go_to_admin_page().add_admin_user()
        time.sleep(30)


