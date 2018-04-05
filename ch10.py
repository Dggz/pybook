
import importlib
math = importlib.import_module('math')
math.sin(2)

# mostly needed if import wrapping will be used

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

#
# fib = load_module('http://localhost:15000/fib.py')
# fib.fib(10)
# spam = load_module('http://localhost:15000/spam.py')
# spam.hello('Guido')
# fib
# spam

"""
As you can see, it "works" for simple modules. However, it’s not plugged into 
the usual import statement, and extending the code to support more advanced 
constructs, such as packages, would require additional work.

A much slicker approach is to create a custom importer. The first way to do 
this is to create what’s known as a meta path importer. Here is an example:"""

"""
#
# urlimport.py
# urlimport.py
# urlimport.py
#
"""
# importing currently fails
import fib

# Load the importer and retry (it works)
import urlimport
urlimport.install_meta('http://localhost:15000')
import fib

import spam

import grok.blah

grok.blah.__file__


"""
This particular solution involves installing an instance of a special finder 
object UrlMetaFinder as the last entry in sys.meta_path. Whenever modules are 
imported, the finders in sys.meta_path are consulted in order to locate the 
module. In this example, the UrlMetaFinder instance becomes a finder of last 
resort that’s triggered when a module can’t be found in any of the normal locations.

As for the general implementation approach, the UrlMetaFinder class wraps around
a user-specified URL. Internally, the finder builds sets of valid links by 
scraping them from the given URL. When imports are made, the module name is 
compared against this set of known links. If a match can be found, a separate 
UrlModuleLoader class is used to load source code from the remote machine and 
create the resulting module object. One reason for caching the links is to 
avoid unnecessary HTTP requests on repeated imports.

The second approach to customizing import is to write a hook that plugs directly
into the sys.path variable, recognizing certain directory naming patterns. 
Add the following class and support functions to urlimport.py:
"""


# https://web.archive.org/web/20170717123149/http://chimera.labs.oreilly.com:80/books/1230000000393/ch10.html#_problem_180


