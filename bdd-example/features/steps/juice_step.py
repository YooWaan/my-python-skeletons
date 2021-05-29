from behave import given, when, then

@given('I put <juice>,')
def step_impl(context, juice):
    context.fruit = juice

@when('I mix')
def step_impl(context):
    context.juice = f'{context.fruit} juice'

@then('I <juice>')
def step_impl(context, juice):
    assert context.juice == juice
