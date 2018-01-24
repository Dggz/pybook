

n = int(input("Number of tasks: "))
k = int(input("Number of workers: "))

# tw = [[range(i*int(n/k) + int(n/k), i + int(n/k))] for i in range(1, int(n/k))]

# tw = [ i*int(n/k) for i in range(1, k + 1) ]
# tw[-1] = n

tw = [i*int(n/k) for i in range(1, k + 1)]

remaining = n % k
i = 0
while remaining:
    if i == len(tw) - 1:
        i = 0
    tw[i] += 1
    remaining -= 1
    i += 1

import ipdb; ipdb.set_trace()
print()

