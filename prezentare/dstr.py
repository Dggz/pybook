""" """
import heapq
from collections import defaultdict, OrderedDict
from random import randint
from contextlib import suppress
from collections import deque

listdict = defaultdict(list)
tupdict = defaultdict(tuple)
setdict = defaultdict(set)
intdict = defaultdict(int)


#
#   Deque stuff
#

d = deque(maxlen=3)

d.append(1)
d.append(2)
d.append(3)
d.pop()
d.popleft()

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
with open('note.txt') as f:
    for line, prevlines in search(f, 'p', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)

#
#   Naming a Slice
#

######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
#######
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
items[a]
items[a] = [10, 11]
items
del items[a]
items

a = slice(10, 50, 2)
a.start
a.stop
a.step

######### cookbook example is wrong

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])


#
#   heapq
#

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
#
#
#
#   for hwapq to work -> elements need to be hashable
#
#
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

##########################
#   nlargest/smallest special cases -> performs max/min if just one, sorts if more than elements
##########################

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
# heap
heapq.heappop(heap)

#
#   PQueue
#

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


import ipdb
ipdb.set_trace()

pq = PriorityQueue()
pq.push(Item('foo'), 1)
pq.push(Item('bar'), 5)
pq.push(Item('spam'), 4)
pq.push(Item('grok'), 1)
pq.pop()

#
#   Ordered Dict
#

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))

# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))

# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

#
#   Dictionary logic
#

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

# Find keys in common
a.keys() & b.keys()   # { 'x', 'y' }

# Find keys in a that are not in b
a.keys() - b.keys()   # { 'z' }

# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }


