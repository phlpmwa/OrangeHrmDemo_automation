import time

from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest


class Test_PimPage(BaseTest):
    def test_add_employee(self):
        login = LoginPage(self.driver)
        login.do_login().go_to_PIM_page().add_employee()

