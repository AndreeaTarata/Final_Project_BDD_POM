from behave import given, then, when

from pages.home_page import HomePage


@when(u'Logo is displayed')
def step_impl(context):
    print(u'STEP: When Logo is displayed')
    page = HomePage(context.driver)
    assert page.get_logo()


@given(u'Go to form page')
def step_impl(context):
    print(u'STEP: Given Go to form page')


@when(u'I enter first name "Andreea"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Andreea"')


@when(u'I enter first name "Cara"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Cara"')


@when(u'click submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click submit')


@then(u'a success message should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a success message should be displayed')


@when(u'I enter first name "Ion"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Ion"')


@when(u'I enter first name "Creanga"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Creanga"')


@when(u'I enter first name "Ileana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Ileana"')


@when(u'I enter first name "Cosanzeana"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter first name "Cosanzeana"')


@then(u'The form should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The form should be displayed')


@when(u'Go to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Go to home page')


@then(u'The home page be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The home page be displayed')


@then(u'I should see "{keyword}"')
def step_impl(context, keyword):
    print(u'STEP: Then I should see "Welcome to Formy"')
    assert keyword in context.driver.page_source
