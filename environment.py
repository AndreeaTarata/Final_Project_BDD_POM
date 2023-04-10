from behave import fixture, use_fixture
from selenium import webdriver

from pages.home_page import HomePage


@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)
    context.homepage = HomePage(context.driver)
    context.homepage.open()

