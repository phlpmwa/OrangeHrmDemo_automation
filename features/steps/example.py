from behave import *


@given("we have behave installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    assert 2 == 2


@when("we implement {number} tests")
def step_impl(context, number):
    print("hello world")
    assert 1 == 1


@then("behave will test them for us!")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 1 == 1
