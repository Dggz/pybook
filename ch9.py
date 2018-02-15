"""ch9"""
from typing import Iterable

"""
object.__getattr__(self, name)
Called when an attribute lookup has not found the attribute in the usual places
(i.e. it is not an instance attribute nor is it 
found in the class tree for self), name is the attribute name. 
This method should return the (computed) attribute value
or raise an AttributeError exception.

Note that if the attribute is found through the normal mechanism,
__getattr__() is not called. (This is an intentional asymmetry 
between __getattr__() and __setattr__().) This is done both for efficiency 
reasons and because otherwise __getattr__() would have no way to access 
other attributes of the instance. Note that at least for instance variables, 
you can fake total control by not inserting any values in the instance 
attribute dictionary (but instead inserting them in another object).
See the __getattribute__() method below for a way to actually get total control
over attribute access.

object.__getattribute__(self, name)
Called unconditionally to implement attribute accesses for 
instances of the class. If the class also defines __getattr__(), the latter 
will not be called unless __getattribute__() either calls it explicitly or
raises an AttributeError. This method should return the (computed) attribute 
value or raise an AttributeError exception. In order to avoid infinite
recursion in this method, its implementation should always call the 
base class method with the same name to access any 
attributes it needs, for example, object.__getattribute__(self, name).
"""


class Count(object):
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax
        self.current = None

    # def __getattr__(self, item):
    #         self.__dict__[item]=0
    #         return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)
        # note this class subclass object


obj1 = Count(1, 10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)

"""
That is all there is to it. 
Define any of these methods and an object is considered a descriptor and
can override default behavior upon being looked up as an attribute.

If an object defines both __get__() and __set__(), 
it is considered a data descriptor. 
Descriptors that only define __get__() are called non-data descriptors 
(they are typically used for methods but other uses are possible).

Data and non-data descriptors differ in how overrides are 
calculated with respect to entries in an instance’s dictionary.
If an instance’s dictionary has an entry with the same name as a 
data descriptor, the data descriptor takes precedence. If an instance’s 
dictionary has an entry with the same name as a 
non-data descriptor, the dictionary entry takes precedence.

To make a read-only data descriptor, define both __get__() and __set__() 
with the __set__() raising an AttributeError when called. 
Defining the __set__() method with an exception raising placeholder 
is enough to make it a data descriptor.
"""


class Integer:
    def __init__(self, name):
        self.name = name

    #  diff between instance variable and class variables
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    #

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


"""METAPROGRAMMING"""
"""Programming for programmers"""

"""Decorators"""
import time
from functools import wraps
def timethis(func):
    """Decorator that reports the execution time."""
    """annotations and stuff"""
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n: int):
    """Counts down"""
    while n > 0:
            n -= 1


@timethis
def sum_(number: int):
    return sum(range(number))


"""Decorator unwrap"""

"""
Better practice to avoid if multiple decorators have been applied
in 3.3, unwrapping bypasses all the layers,
one at a time in 3.5
"""

from functools import wraps
def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y


"""Decorators that accept arguments"""

from functools import wraps
import logging
def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

"""
Can be tricky

@decorator(x, y, z)
def func(a, b):
    pass

The decoration process evaluates as follows:

def func(a, b):
    pass

func = decorator(x, y, z)(func)
"""


"""Defining a Decorator with User Adjustable Attributes"""

from functools import wraps, partial
import logging

# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


import logging
logging.basicConfig(level=logging.DEBUG)
add(2, 3)

# Change the log message
add.set_message('Add called')
add(2, 3)

# Change the log level
add.set_level(logging.WARNING)
add(2, 3)

"""On multiple levels"""
@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1

"""Defining a Decorator That Takes an Optional Argument"""
"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_discussion_149"
from functools import wraps, partial
import logging
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_150"
"""Enforcing Type Checking on a Function Using a Decorator"""

from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                      raise TypeError(
                        'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, int)
def add(x, y):
    return x + y

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_151"
"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_152"
"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_153"


"Decorators that add arguments to wrapped functions"
"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_154"

"? https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_solution_155"

"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_160"

"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_problem_161"

"""Fix repetitive properties"""
"https://web.archive.org/web/20171130045115/http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_solution_164"


