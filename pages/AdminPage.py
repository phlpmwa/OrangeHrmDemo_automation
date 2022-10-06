import time

from pages.BasePage import BasePage


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_admin_user(self):
        self.click("admin_add_XPATH")
        self.click("user_role_select_XPATH")
        self.click("admin_admin_XPATH")
        self.click("status_select_XPATH")
        self.click("status_enabled_XPATH")
        self.type("employee_name_CSS", "Philip Mwaura Mwaure")
        self.type("admin_username_XPATH", "mwash123")
        self.type("admin_password_XPATH", "Phlp@290")
        self.type("admin_password_confirm_XPATH", "Phlp@290")
        self.click("admin_save_btn_XPATH")
