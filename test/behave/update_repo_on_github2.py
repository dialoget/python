import sys
sys.path.append('../')
#from data.env import GITHUB_API_URL
from src.update_repo_on_github2 import update_repo_on_github2
from data.prompt import *
#from data.map import *

from behave import given, when, then

@given('a user has navigated to the login page')
def step_impl(context):
    context.browser.visit(context.config.base_url)

@when('the user enters a correct username and password')
def step_impl(context):
    context.browser.fill_form_with_correct_credentials()

@then('they are redirected to their dashboard')
def step_impl(context):
    assert context.browser.on_dashboard()

@then('they see a welcome message')
def step_impl(context):
    assert context.browser.shows_welcome_message()
