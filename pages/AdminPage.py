import time

from pages.BasePage import BasePage


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_admin_user(self):
        self.click("admin_add_XPATH")
        self.click("employee_name_CSS")
        self.click("user_role_select_XPATH")
        self.click("admin_admin_XPATH")
        self.type("employee_name_CSS", "Philip")
        self.type("admin_username_XPATH", "Pnm")
        #self.click("admin_save_btn_XPATH")
