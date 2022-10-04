from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest


class Test_LoginPage(BaseTest):
    def test_login(self):
        login = LoginPage(self.driver)
        login.do_login()
        home_page = HomePage(self.driver)
        assert "OrangeHRM" == home_page.get_title()
        print("this is the title ", home_page.get_title())

