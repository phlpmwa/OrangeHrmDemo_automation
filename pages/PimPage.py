import time

from pages.BasePage import BasePage


class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_employee(self):
        self.click("pim_add_XPATH")
        self.type("pim_first_name_XPATH", "Philip")
        self.type("pim_middle_name_XPATH", 'Mwaura')
        self.type("pim_last_name_XPATH", 'Mwaure')
        self.type("pim_employee_id_XPATH", '0900')
        self.type("pim_profile_picture_CSS", "C:/Users/Phlp/Pictures/image_1.png")
        time.sleep(5)
        self.click("pim_save_btn_XPATH")

    def delete_employees(self):
        for _ in range(10):
            if self.find_elements("pim_trash_icon_CSS"):
                self.click("pim_trash_icon_CSS")
                self.click("pim_confirm_delete_XPATH")
