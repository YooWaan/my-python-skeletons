from behave import given, when, then

@given('I put {thing} ,')
def put_thing(context, thing):
    context.fruit = thing


@when('I mix')
def mix_it(context):
    context.juice = f'{context.fruit} juice'


@then('it should transform into {juice}')
def done_juice(context, juice):
    assert context.juice == juice


@given('果物を {thing} 用意します')
def put_thing(context, thing):
    context.fruit = thing


@when('混ぜます')
def mix_it(context):
    context.juice = f'{context.fruit} juice'


@then('{juice} ができました')
def done_juice(context, juice):
    assert context.juice == juice
