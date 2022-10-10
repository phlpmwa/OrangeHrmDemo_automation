import time

from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest


class Test_AdminPage(BaseTest):
    def test_add_admin_user(self):
        login = LoginPage(self.driver)
        homepage = login.do_login()
        admin_page = homepage.go_to_admin_page()
        admin_page.add_admin_user()


