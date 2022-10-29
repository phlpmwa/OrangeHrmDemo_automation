import time

from behave import *
from selenium.webdriver.common.by import By

from features.pageObjects.LoginPage import LoginPage
from utilities import configreader


@given("user is on login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.login = LoginPage(context.driver)
    context.login.open_url(configreader.read_config("base-url", "orange_hrm_demo_site"))


@when('user enter username')
def step_impl(context):
    """
    :param username:
    :type context: behave.runner.Context
    """
    context.login.enter_username("Admin")
    print("hello world")
    print(u'STEP: When user enter username')


@then('user enter password')
def step_impl(context):
    """
    :param password:
    :type context: behave.runner.Context
    """
    context.login.enter_password("admin123")
    print(u'STEP: And  user enter password')


@step("user user click login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(4)
    context.login.submit_login()
    print(u'STEP: And  user user click login button')
    time.sleep(10)


@then("home page should open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then home page should open')
