
#### printing with diff separators/endlines
# print('ACME', 50, 91.5)
# print('ACME', 50, 91.5, sep=',')
# print('ACME', 50, 91.5, sep=',', end='!!\n')

# end=  can be used to suppress \n when printing

for i in range(5):
    print(i, end=' ')

print(','.join(('ACME', '50', '91.5')))

row = ('ACME', 50, 91.5)
# print(','.join(row))
print(*row, sep=',')

b = b'Hello World'

for c in b:
    print(c)
import os
files = os.listdir('.')

with open('somefile.txt', 'rt') as f:
    data = f.read()

with open('somefile.txt', 'wt') as f:
    f.write('linia 1')
    f.write('linia 2')

with open('somefile.txt', 'at') as f:
    f.write('linia 6')

with open('somefile.txt', 'rt', encoding='latin-1') as f:
    asd = f.readline()

#
#   use 'with' instead of just open()
#

with open('somefile.txt', 'rt') as f: # needs to be in text mode !!!
    print('Hello World!', file=f)


with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

# X for creating a file that does not exist
with open('somefilens', 'xt') as f:
    f.write('Hello\n')

path = 'somefile.txt'

os.path.join('..', 'out', 'vmax_out.xlsx')
os.path.exists(path)
os.path.getmtime(path)
os.listdir('..')

import time
time.ctime(os.path.getmtime(path))

# bad filenames

def bad_filename(filename):
    return repr(filename)[1:-1]
