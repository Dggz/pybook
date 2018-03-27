
import importlib
math = importlib.import_module('math')
math.sin(2)

# https://web.archive.org/web/20170717123149/http://chimera.labs.oreilly.com:80/books/1230000000393/ch10.html#_problem_179

"""
First, a serious disclaimer about security. The idea discussed in this recipe
would be wholly bad without some kind of extra security and authentication 
layer. That said, the main goal is actually to take a deep dive into the inner 
workings of Python’s import statement. If you get this recipe to work and 
understand the inner workings, you’ll have a solid foundation of customizing 
import for almost any other purpose. With that out of the way, let’s carry on.
"""


'''
bash % cd testcode
bash % python3 -m http.server 15000
Serving HTTP on 0.0.0.0 port 15000 ...
'''

from urllib.request import urlopen
ur = urlopen('http://localhost:15000/fib.py')
data = ur.read().decode('utf-8')
print(data)


import imp
import urllib.request
import sys

def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


# ???

# https://web.archive.org/web/20170717123149/http://chimera.labs.oreilly.com:80/books/1230000000393/ch10.html#_problem_180


