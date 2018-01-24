"""
Created on Dec 15, 2016

@author: Dggz
"""

def file_print(msg, output_file):
    output_file.write(msg + '\n')
    print(msg)


f = open('cabana.txt', 'w')

pretCabana = int(input("\nPret cabana: ")) # ex: 6000
s1 = float(pretCabana/3)
f.write("\nPret cabana: {}".format(pretCabana))
file_print("\nPret pe seara: " + str(round(s1)), f)

p1 = int(input("\nPersoane seara 1: "))
p2 = int(input("\nPersoane seara 2: "))
p3 = int(input("\nPersoane seara 3: "))
f.write("\nPersoane seara 1: {}"
        "\nPersoane seara 2: {}"
        "\nPersoane seara 3: {}\n".format(p1, p2, p3))
# print('---input done---')

s1, s2 , s3 = round(s1/p1), \
              round(s1/p2), \
              round(s1/p3)

tbl  = "\nPret seara 1/pers: " + str(s1)
tbl += "\nPret seara 2/pers: " + str(s2)
tbl += "\nPret seara 3/pers: " + str(s3)
file_print(tbl, f)
# print('---intermediary done---')

s2ind = s1 + s2 + 2
s3ind = s2ind + s3

final = '\nPret pt o seara: {}\n'.format(s1)
final += '\nPret pt 2 seri: {}\n'.format(s2ind)
final += '\nPret pt 3 seri: {}\n'.format(s3ind)
file_print(final, f)
print('---program done---')

test_total = s3ind * p3 + s2ind * (p2 - p3) + s1 * (p1 - p2)

if test_total in range(pretCabana, pretCabana + 101):
    file_print('---test phase---\nTest passed, rounded total: {}'.format(test_total), f)
else:
    file_print('Test failed, formula wrong, rounded total: {}'.format(test_total), f)

f.close()
