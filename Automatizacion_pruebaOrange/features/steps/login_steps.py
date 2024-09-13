from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage

@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.login_page = LoginPage(context.driver)

@when('I enter username and password')
def step_when_i_enter_username_and_password(context):
    context.login_page.enter_username('Admin')
    context.login_page.enter_password('admin123')

@when('I click on login')
def step_when_i_click_on_login(context):
    context.login_page.click_login_button()

@when('I navigate to Recruitment')
def step_when_i_navigate_to_recruitment(context):
    context.recruitment_page = RecruitmentPage(context.driver)
    context.recruitment_page.click_recruitment_menu()

@then('I should see the Recruitment page')
def step_then_i_should_see_the_recruitment_page(context):
    assert 'recruitment' in context.driver.current_url
    context.driver.quit()

@then('I click on the Add button')
def step_impl(context):
    context.recruitment_page.click_add_button()