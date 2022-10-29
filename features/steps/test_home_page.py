from behave import *

from features.pageObjects.HomePage import HomePage

use_step_matcher("re")


@given("user is logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps('''
   Given user is on login page
    When user enter username
    Then  user enter password
    And  user user click login button
    Then home page should open
        ''')


@when("home page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When home page is opened')


@step("user click admin link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home = HomePage(context.driver)
    context.home.go_to_admin_page()


@then("admin page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then admin page is opened')
