


items = iter([1, 2, 3])

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):  # works on more than 2
    print(x,y)

xpts = [1, 5, 4, 2]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)

from itertools import zip_longest
xpts = [1, 5, 4, 2]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip_longest(xpts, ypts): # fillvalue=
    print(x,y)


headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
sd = dict(zip(headers,values))

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)

with open('note.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

with open('note.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


def countdown(n):
    print('Starting to count from', n)
    yield 'first'
    yield 'second'
    while n > 0:
        yield n
        n -= 1
    print('Done!')

reversed([1, 2, 3, 4 ])


from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('prezentare/note.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

def count(n):
    while True:
        yield n
        n += 1

ad = count(0)

#
# ad[10:20]
# won't work

import itertools

for x in itertools.islice(ad, 10, 20):
    print(x)

# interesting if some next() 's were called before the islice

with open('note.txt') as f:
    for line in f:
        print(line, end='')

from itertools import dropwhile
with open('note.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
         print(line, end='')

# instead of

with open('note.txt') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    while line:
        print(line, end='')
        line = next(f, None)

items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

######
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)