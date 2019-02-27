from behave import *
from login_page import LoginPage
import time


# scenario:succeed
@given('go to login page')
def step_impl(context):
    context.login_page = LoginPage(context.dr)
    context.login_page.url = 'http://localhost/wordpress/wp-admin'
    context.login_page.navigate()


@when('login with {username} {password}')
def step_impl(context, username, password):
    context.dashboard_page = context.login_page.user_login(username, password)


@then('redirect to dashboard page')
def step_impl(context):
    assert 'wp-admin' in context.dr.current_url
    assert context.login_page.username() in context.login_page.greeting_link().text


# scenario:failed
@when('incorrect login with {username} and {password} again')
def step_impl(context, username, password):
    if username == 'empty':
        username = ''
    if password == 'empty':
        password = ''
    context.dashboard_page = context.login_page.clear_and_user_login(username, password)
    time.sleep(3)


@then('display error {message}')
def step_impl(context, message):
    displayed_msg = context.login_page.error_message()
    assert displayed_msg == message