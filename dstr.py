""" """
from collections import defaultdict
creddict = defaultdict(list)
subjdict = defaultdict(tuple)
fulldict = defaultdict(set)

print()
from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
with open('note.txt') as f:
    import ipdb; ipdb.set_trace()
    for line, prevlines in search(f, 'p', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)