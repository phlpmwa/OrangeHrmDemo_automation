from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
