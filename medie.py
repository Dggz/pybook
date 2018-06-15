""" """
from collections import defaultdict
creddict = defaultdict(list)
subjdict = defaultdict(tuple)
fulldict = defaultdict(list)
with open('note.txt', 'r') as note:
    for line in note.readlines():
        *_, credit, nota = line.split()
        #
        # *_, credit, nota = line
        #
        creddict[int(credit)].append(int(nota))

        *materie, credit, nota = line.split()
        mat = ' '.join([mkey.capitalize() for mkey in materie])
        subjdict[mat] = (int(credit), int(nota))
        fulldict[int(credit)].append((mat, int(nota)))

ponds = 0
suma = 0
for key in creddict.keys():
    ponds += key*sum([nota for nota in creddict[key]])
    suma += key*len(creddict[key])

medie = ponds / suma
# print(medie)
fponds = []
fsuma = 0
fmax = ('', 0, 0)
for key in fulldict.keys():
    for materie, nota in fulldict[key]:
        fponds.append(nota*key)
        if nota*key > fmax[1]:
            fmax = materie, nota*key, nota
        fsuma += key

print('Most significant subject for average: {}: {}'.format(fmax[0], fmax[2]))
print('Most significant subject for average: {subj}: {mark}'.format(subj=fmax[0], mark=fmax[2]))
import ipdb; ipdb.set_trace()
import ipdb; ipdb.set_trace()

fmedie = sum(fponds) / fsuma
# print(fmedie)
