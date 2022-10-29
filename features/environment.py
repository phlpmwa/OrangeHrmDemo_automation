import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from utilities import configreader


def before_scenario(context, driver):
    if configreader.read_config("base-url", "browser") == "chrome":
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
