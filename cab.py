
def file_print(msg, output_file):
    output_file.write(msg + '\n')
    print(msg)


def round_ten(number):
    rounded = round(number, -1)
    return rounded if number < rounded else rounded + 10


f = open('cab.txt', 'w')

pret_cabana = 8500 # pret_cabana = int(input("\nPret cabana: ")) # ex: 6000
s1 = float(pret_cabana / 3)
f.write("\nPret cabana: {}".format(pret_cabana))
file_print("\nPret pe seara: " + str(round(s1)), f)

p1 = int(input("\nPersoane o seara: "))
p2 = int(input("\nPersoane 2 seri: ")) # p2 = p1
p3 = int(input("\nPersoane 3 seri: "))

f.write("\nPersoane seara 1: {}"
        "\nPersoane seara 2: {}"
        "\nPersoane seara 3: {}\n".format(p3 + p2, p3 + p2, p3 + p1))

s1, s2, s3 = round(s1/(p3 + p2) + 1), round(s1/(p3 + p2)), round(s1/(p3 + p1))

tbl = "\nPret seara 1/pers: " + str(s1)
tbl += "\nPret seara 2/pers: " + str(s2)
tbl += "\nPret seara 3/pers: " + str(s3)
# f.write(tbl)
# file_print(tbl, f)

s2ind = s1 + s2

s2ind = round_ten(round(s2ind / 2 * 2.25))

s3ind = round_ten((pret_cabana - (p2 * s2ind + p1 * s1 )) / p3)

cap = 550

if s3ind > cap:
    s3ind = cap
    rest = pret_cabana - p3 * s3ind - p1 * s1
    rounded = round(rest / p2, -1)
    s2ind = rounded if rest / p2 < rounded else rounded + 10


final = '\nPret pt o seara: {}\n'.format(s1)
final += '\nPret pt 2 seri: {}\n'.format(s2ind)
# final = '\nPret pt 2 seri: {}\n'.format(s2ind)
final += '\nPret pt 3 seri: {}\n'.format(s3ind)
file_print(final, f)
print('---program done---')

test_total = s3ind * p3 + s2ind * p2 + s1 * p1

if test_total in range(pret_cabana, pret_cabana + 101):
    file_print('---test phase---\nTest passed, rounded total: {}'.format(test_total), f)
else:
    file_print('Test failed, formula wrong, rounded total: {}'.format(test_total), f)

f.close()
