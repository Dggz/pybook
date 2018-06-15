import ipdb; ipdb.set_trace()
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# Sample use
avg(1, 2)          # 1.5
avg(1, 2, 3, 4)    # 2.5

import ipdb; ipdb.set_trace()
print()

import html
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                  name=name,
                  attrs=attr_str,
                  value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)#, pythonics=2346345345234)
import ipdb; ipdb.set_trace()

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')

import ipdb; ipdb.set_trace()

def anyargs(*args, **kwargs):
    print(args)      # A tuple
    print(kwargs)    # A dict

anyargs(1, 2, 3, d=1, e=2, f=3)
import ipdb; ipdb.set_trace()
print()

"""

A * argument can only appear as the last positional argument in a function definition.
A ** argument can only appear as the last argument. A subtle aspect of function definitions
is that arguments can still appear after a * argument.

"""
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass

import ipdb; ipdb.set_trace()

def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

import ipdb; ipdb.set_trace()

def add(x:int, y:int) -> int:
    return x + y

# add.__annotations__

import ipdb; ipdb.set_trace()

def spam(a, b=42):
    print(a, b)

import ipdb; ipdb.set_trace()
x = 42
def spam(a, b=x):
    print(a, b)

spam(1)

x = 23     # Has no effect
spam(1)

import ipdb; ipdb.set_trace()

def spam(a, b=[]): # NOOOOOOOOOOO
    print(b)
    return b

x = spam(1)
x.append(99)
x.append('Yow!')
spam(1)       # Modified list gets returned!
import ipdb; ipdb.set_trace()

def spam(a, b=None):
    if b is None:      # might get a false positive otherwise
        b = []
    print(b)

import ipdb; ipdb.set_trace()


add = lambda x, y: x + y

# return list(filter(
#         lambda file_content: any(
#             fnmatch(file_content[0], pattern) for pattern in patterns),
#         raw_content))

import ipdb; ipdb.set_trace()
names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())

import ipdb; ipdb.set_trace()

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

import ipdb; ipdb.set_trace()

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)

import ipdb; ipdb.set_trace()
print()
