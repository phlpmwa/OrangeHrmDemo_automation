from features.pageObjects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_admin_page(self):
        self.click("admin_link_XPATH")
