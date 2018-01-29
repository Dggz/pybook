"""ch9"""

"""

object.__getattr__(self, name)
Called when an attribute lookup has not found the attribute in the usual places
(i.e. it is not an instance attribute nor is it found in the class tree for self).
name is the attribute name. This method should return the (computed) attribute value
or raise an AttributeError exception.

Note that if the attribute is found through the normal mechanism,
__getattr__() is not called. (This is an intentional asymmetry between __getattr__()
and __setattr__().) This is done both for efficiency reasons and because otherwise
__getattr__() would have no way to access other attributes of the instance.
Note that at least for instance variables, you can fake total control by not inserting
any values in the instance attribute dictionary
(but instead inserting them in another object).
See the __getattribute__() method below for a way to actually get total control
over attribute access.

object.__getattribute__(self, name)
Called unconditionally to implement attribute accesses for instances of the class. If the class also defines __getattr__(), the latter will not be called unless __getattribute__() either calls it explicitly or raises an AttributeError. This method should return the (computed) attribute value or raise an AttributeError exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, object.__getattribute__(self, name).

"""

"""Example"""

"""

That is all there is to it. 
Define any of these methods and an object is considered a descriptor and 
can override default behavior upon being looked up as an attribute.

If an object defines both __get__() and __set__(), it is considered a data descriptor. 
Descriptors that only define __get__() are called non-data descriptors 
(they are typically used for methods but other uses are possible).

Data and non-data descriptors differ in how overrides are calculated with respect 
to entries in an instance’s dictionary. If an instance’s dictionary has an entry 
with the same name as a data descriptor, the data descriptor takes precedence. 
If an instance’s dictionary has an entry with the same name as a non-data descriptor, 
the dictionary entry takes precedence.

To make a read-only data descriptor, define both __get__() and __set__() with the __set__() 
raising an AttributeError when called. Defining the __set__() method with an exception 
raising placeholder is enough to make it a data descriptor.

"""

"""Example"""

