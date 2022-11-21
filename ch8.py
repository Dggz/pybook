

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x}, {0.y})'.format(self)

    def __str__(self):
        return '({0.x}, {0.y})'.format(self)

pr = Pair(3, 4)
pr
print(pr)
print('p is {0!r}'.format(pr))
print('p is {0}'.format(pr))
# !r takes the __repr__


formats_ = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }


# if you have a lot of instances use __slots__
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.hour = 1

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = formats_[code]
        return fmt.format(d=self)

#
#  Defineste cum va arata o instanta cand e un argument a functiei format
#


dt = Date(2012, 12, 21)
format(dt)
format(dt, 'mdy')
'The date is {:ymd}'.format(dt)
'The date is {:mdy}'.format(dt)
'The date is {:dmy}'.format(dt)


from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__() executes: connection closed


# managed attributes
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


ps = Person('Guido')
ps.first_name       # Calls the getter
# ps.first_name = 42

"""
Don't use these as you would use getters/setters in java

also don't use it the same way for a different attribute (property on first_name and last_name)

use them if you need extra processing

setters and getters can be used explicitly for integration
"""

class BadPerson:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius



# Descriptor attribute for an integer type-checked attribute
"""
A descriptor is a class that implements the three core attribute access operations (get, set, and delete)
    in the form of __get__(), __set__(), and __delete__() special methods. 
These methods work by receiving an instance as input. 
The underlying dictionary of the instance is then manipulated as appropriate.
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

pt = Point(2,3)
pt.x      # Calls Point.x.__get__(p, Point)
Point.x  # Calls Point.


lazy_prop = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_solution_128'

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


data_structs = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_129'

"""
Useful when writing a program built around a large number 
of small data structures. It leads to much less code than manually 
writing __init__().

Downside on documentation and IDE help
"""

class Structure:
    # Class variable that specifies expected fields
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x','y']

    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2



abstract_stuff = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_130'
"""
Although ABCs facilitate type checking, it’s not something that you should overuse in a program.
At its heart, Python is a dynamic language that gives you great flexibility. 
Trying to enforce type constraints everywhere tends to result in code that is more complicated
than it needs to be. You should embrace Python’s flexibility.
"""

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# istrm = IStream()

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print(maxbytes)

    def write(self, data):
        print(data)


data_or_type_system = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_131'


custom_containers = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_132'
attr_access = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_133'
no_init = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_135'
mixins = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_136'

state_machines_or_objects = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_137'


class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')


class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self, data):
        print(f'writing {data}')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


visitor = 'http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_139'
