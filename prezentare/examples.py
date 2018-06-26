
import re

p = 4, 5
p = (4, 5)
x, y = p
# x, y, z = p
x
y

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data

otherdata = [ 'ACME', 50, 91.1, 2012, 12, 21 ]
name, shares, price, *date = otherdata


s = 'Hello'
a, b, c, d, e = s

f, _, h, _, k = s

text = 'one PYTHON, two python, three Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


import textwrap

print(textwrap.fill(s, 70))

print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent='    '))

print(textwrap.fill(s, 40, subsequent_indent='    '))
