from behave import *
from app.calculator import Calculator


@given(u'we have a calculator')
def step_impl(context):
    context.myCalc = Calculator()

@when(u'we give 2 Ints {x} and {y}')
def step_impl(context, x, y):
    context.result=context.myCalc.add(int(x),int(y))

@then(u'we get the int result of {Res}')
def step_impl(context,Res):
    assert(context.result == int(Res))


@when(u'we give 2 Floats {x} and {y}')
def step_impl(context, x, y):
    context.result=context.myCalc.add(float(x),float(y))

@then(u'we get the float result of {Res}')
def step_impl(context,Res):
    assert(context.result == float(Res))


#@when(u'we give <Val1> and <Val2>')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: When we give <Val1> and <Val2>')
#
#
#@then(u'we get a failure')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then we get a failure')
#
#    