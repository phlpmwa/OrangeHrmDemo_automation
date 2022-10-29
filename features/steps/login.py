import time

from behave import *
from selenium.webdriver.common.by import By


@given("user is on login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('user enter "{username}"')
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(by=By.NAME, value="username").send_keys(username)
    print("hello world")
    print(u'STEP: When user enter username')


@step('user enter "{password}"')
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(by=By.NAME, value="password").send_keys(password)
    print(u'STEP: And  user enter password')


@step("user user click login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(by=By.XPATH, value="//button").click()
    print(u'STEP: And  user user click login button')


@then("home page should open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then home page should open')
