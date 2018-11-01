## Overview of decorators

Decorators are functions that takes one argument and returns something useful.

They can dynamically alter the functionality of a function/method/class.

They are mostly used to modify the behavior of the code before or after a function execution, without the need to modify the actual function itself, augmenting the original functionality.


In simple term, this is how a decorator looks
```
@mydecorator
def myfunc():
    pass
```
This is equivalent to
```
def myfunc():
    pass
myfunc = mydecorator(myfunc)
```

#### Simple decorator function
```
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "{0} is a nice person".format(name)

print(get_text("Ram"))
```

### Its now time to learn about functions and methods in python

*Python Function*
* Function is block of code that is also called by its name. (independent)
* The function can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
* It may or may not return any data.
* Function does not deal with Class and its instance concept.
```
def Subtract (a, b): 
    return (a-b) 
  
print( Subtract(10, 12) ) # prints -2 
```

*Python Method*
* Method is called by its name, but it is associated to an object (dependent).
* A method is implicitly passed the object on which it is invoked.
* It may or may not return any data.
* A method can operate on the data (instance variables) that is contained by the corresponding class
```
# Python 3  User-Defined  Method 
class ABC : 
    def method_abc (self): 
        print("I am in method_abc of ABC class. ") 
  
class_ref = ABC() # object of ABC class 
class_ref.method_abc()
```

For more details check [here](https://www.geeksforgeeks.org/difference-method-function-python/)

#### Simple decorator method
```
def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "Sita"
        self.surname = "Ram"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.surname

my_person = Person()
print(my_person.get_fullname())
```

#### Common decorator for function/method

This can be done by putting [args and \*kwargs](https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments) as parameters for the wrapper, then it can accept any arbitrary number of arguments and keyword arguments.
```
def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper
```

#### Decorators with parameters
```
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print get_text("Ram")
```
However debugging this is difficult since the wrapper function does not carry the name, module and docstring of the original function. Based on the example above if we do:
```
print get_text.__name__
# Outputs func_wrapper rather than get_text
```
Wraps is a decorator for updating the attributes of the wrapping function(func_wrapper) to those of the original function(get_text). This is as simple as decorating func_wrapper by @wraps(func). This is available in Functools

```
from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kwargs))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print(get_text.__name__) # get_text
print(get_text.__doc__) # returns some text
print(get_text.__module__) # __main__
```

#### Final decorator with updates before and after a function
```
from functools import wraps

def mydecorator_not_actually(count):
    def true_decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            for i in range(count):
                print("Before decorated function")
            r = f(*args, **kwargs)
            for i in range(count):
                print("After decorated function")
            return r
        return wrapped
    return true_decorator

@mydecorator_not_actually(count=5)
def myfunc(myarg):
    print("my function", myarg)
    return "return value"

r = myfunc('myfunc')
print(r)
```
