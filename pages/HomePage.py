import time

from pages.AdminPage import AdminPage
from pages.BasePage import BasePage
from pages.BuzzPage import BuzzPage
from pages.DashboardPage import DashboardPage
from pages.DirectoryPage import DirectoryPage
from pages.LeavePage import LeavePage
from pages.MaintenancePage import MaintenancePage
from pages.MyInfoPage import MyInfoPage
from pages.PerformancePage import PerformancePage
from pages.PimPage import PimPage
from pages.RecruitmentPage import RecruitmentPage
from pages.TimePage import TimePage


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

    def go_to_Leave_page(self):
        self.click("leave_link_XPATH")
        return LeavePage(self.driver)

    def got_to_time_page(self):
        self.click("time_link_XPATH")
        return TimePage(self.driver)

    def got_to_recruitment_page(self):
        self.click("recruitment_link_XPATH")
        return RecruitmentPage(self.driver)

    def go_to_myInfo_page(self):
        self.click("my_info_link_XPATH")
        return MyInfoPage(self.driver)

    def go_to_performance_page(self):
        self.click("performance_link_XPATH")
        return PerformancePage(self.driver)

    def go_to_dashboard_page(self):
        self.click("dashboard_link_XPATH")
        return DashboardPage(self.driver)

    def go_to_directory_page(self):
        self.click("directory_link_XPATH")
        return DirectoryPage(self.driver)

    def go_to_maintenance_page(self):
        self.click("maintenance_link_XPATH")
        return MaintenancePage(self.driver)

    def go_to_buzz_page(self):
        self.click("buzz_link_XPATH")
        return BuzzPage(self.driver)
