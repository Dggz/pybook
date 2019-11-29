
# variable unpacking

p = 4, 5
p = (4, 5)
x, y = p
# error
# x, y, z = p
x
y

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data

otherdata = ['ACME', 50, 91.1, 2012, 12, 21]
name, shares, price, *date = otherdata

# also at the beginning
sales_record = [1, 2, 3, 4, 23, 45, 3, 345]
*trailing_qtrs, current_qtr = sales_record

# this way we don't have to do cumbersome processing like below
records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


#  deque

from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q
deque([1, 2, 3], maxlen=3)
q.append(4)
q
deque([2, 3, 4], maxlen=3)
q.append(5)
q
deque([3, 4, 5], maxlen=3)


#  deque example

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
# if __name__ == '__main__':
with open('prezentare/somefile.txt', 'r') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)



indent = 'Hello'
a, b, c, d, e = indent

f, _, h, _, k = indent

import re


text = 'one PYTHON, two python, three Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)


indent = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


import textwrap

print(textwrap.fill(indent, 70))

print(textwrap.fill(indent, 40))

print(textwrap.fill(indent, 40, initial_indent='    '))

print(textwrap.fill(indent, 40, subsequent_indent='    '))
