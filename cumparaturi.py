"""
Created on Dec 15, 2016

@author: Dggz
"""
from collections import defaultdict

categories = defaultdict(tuple)
total_peeps = 0
with open('cats.txt', 'r') as inp:
    for i in inp.readlines():
        if len(i) > 1:
            *category, suma, peeps = i.split()
            if category[0] == 'total':
                total_peeps = int(peeps)
            categories[' '.join(category)] = int(suma) + 1, int(peeps)

with open('banidedat.txt', 'w') as f:
    final_sum = 0
    for cat in categories:
        if cat != 'total':
            final_sum += round(categories[cat][0] / (categories[cat][1] + total_peeps), 2) * categories[cat][1]
            f.write('{}: -> {}\n'.format(
                cat, round(categories[cat][0] / (categories[cat][1] + total_peeps), 2)))
            print('{}: -> {}'.format(
                cat, round(categories[cat][0] / (categories[cat][1] + total_peeps), 2)))

    f.write('{}: -> {}\n'.format(
        'total', round((categories['total'][0] - final_sum) / categories['total'][1], 2)))
    print('{}: -> {}'.format(
        'total', round((categories['total'][0] - final_sum) / categories['total'][1], 2)))

final_sum += categories['total'][0] - final_sum
print(final_sum)



