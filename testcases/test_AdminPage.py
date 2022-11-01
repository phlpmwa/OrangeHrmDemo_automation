import time

from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest
from pytest_testrail.plugin import  pytestrail


class Test_AdminPage(BaseTest):
    @pytestrail.case('C1', 'C2')
    def test_add_admin_user(self):
        login = LoginPage(self.driver)
        homepage = login.do_login()
        admin_page = homepage.go_to_admin_page()
        admin_page.add_admin_user()


