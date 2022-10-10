from pages.LoginPage import LoginPage
from testcases.BaseTest import BaseTest


class Test_HomePage(BaseTest):
    def test_go_to_home_links(self):
        login = LoginPage(self.driver)
        home = login.do_login()
        home.go_to_admin_page()
        home.go_to_PIM_page()
        home.go_to_Leave_page()
        home.got_to_time_page()
        home.got_to_recruitment_page()
        home.go_to_myInfo_page()
        home.go_to_performance_page()
        #home.go_to_maintenance_page()
        home.go_to_directory_page()
        home.go_to_dashboard_page()
        home.go_to_buzz_page()

