from decimal import Decimal, localcontext
import math


round(1.23, 1)
round(1.23)
round(1.27, 1)
round(-1.27, 1)
round(1.25361, 3)
round(125361, -1)
round(125361, -2)

# don't use it to format numbers
# don't use it to format numbers
# don't use it to format numbers

x = 1.23456
format(x, '0.2f')
format(x, '0.3f')
format(-x, '0.1f')
'value is {:0.3f}'.format(x)

x = 1234.56789

# Two decimal places of accuracy
format(x, '0.2f')
# Right justified in 10 chars, one-digit accuracy
format(x, '>10.1f')
# Left justified
format(x, '<10.1f')
# Centered
format(x, '^10.1f')
# Inclusion of thousands separator
format(x, ',')
format(x, '0,.1f')

#
# Lamer formatting
#

print('%0.2f' % x)

#
# Lamer formatting
#

swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators)

"""

Also, resist the urge to round floating-point numbers to "fix" 
perceived accuracy problems. 
For example, you might be inclined to do this:

"""

a = 2.1
b = 4.2
c = a + b

c = round(c, 2)      # "Fix" result (???)

"""
For most applications involving floating point, 
it’s simply not necessary (or recommended) to do this. 
Although there are small errors introduced into calculations, 
the behavior of those errors are understood and tolerated. 
If avoiding such errors is important (e.g., in financial applications, perhaps), 
consider the use of the decimal module, which is discussed in the next recipe.
"""

a = Decimal('4.2')
b = Decimal('2.1')
a + b

print(a + b)

eq = (a + b) == Decimal('6.3')

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

"""

Newcomers to Python might be inclined to use the decimal 
module to work around perceived accuracy problems with the 
float data type. However, it’s really important to understand
your application domain. If you’re working with science
or engineering problems, computer graphics, or most things
of a scientific nature, it’s simply more common to use the 
normal floating-point type. For one, very few things in the 
real world are measured to the 17 digits of accuracy that 
floats provide. Thus, tiny errors introduced in 
calculations just don’t matter. Second, the performance 
of native floats is significantly faster—something that’s 
important if you’re performing a large number of calculations.

"""

nums = [1.23e+18, 1, -1.23e+18]
sum(nums)

math.fsum(nums)


x = 1234
bin(x)
oct(x)
hex(x)

format(x, 'b')
format(x, '0')
format(x, 'x')

int('4d2', 16)
int('010100101', 2)

import os
# os.chmod('script.py', 0755)
# os.chmod('script.py', 0o755)

a = complex(2, 4)
b = 3 - 5j
a.real
a.imag
a.conjugate()
a + b
a-b
abs(a)

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
a + 2
np.sin(a)

import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values)

# maybe show some randint and stuff

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days

c.seconds

c.seconds / 3600

c.total_seconds() / 3600
