
def file_print(msg, output_file):
    output_file.write(msg + '\n')
    print(msg)


def round_ten(number):
    rounded = round(number, -1)
    return rounded if number < rounded else rounded + 10


f = open('cabana2nopti.txt', 'w')

pret_cabana = int(input("\nPret cabana: "))  # ex: 6000
s1 = float(pret_cabana / 2)
f.write("\nPret cabana: {}".format(pret_cabana))
file_print("\nPret pe seara: " + str(round(s1)), f)

p1 = int(input("\nPersoane seara 1: "))
p2 = int(input("\nPersoane seara 2: "))

f.write("\nPersoane seara 1: {}"
        "\nPersoane seara 2: {}\n".format(p1, p2))

s1, s2 = round(s1/p1), round(s1/p2)

tbl = "\nPret seara 1/pers: " + str(s1)
tbl += "\nPret seara 2/pers: " + str(s2)
file_print(tbl, f)

s2ind = s1 + s2

final = '\nPret pt o seara: {}\n'.format(s1)
final += '\nPret pt 2 seri: {}\n'.format(s2ind)
file_print(final, f)
print('---program done---')

test_total = s2ind * p2 + s1 * (p1 - p2)

if test_total in range(pret_cabana, pret_cabana + 101):
    file_print(
        '---test phase---\nTest passed, rounded total: {}'.format(test_total), f
    )
else:
    file_print(
        'Test failed, formula wrong, rounded total: {}'.format(test_total), f
    )

f.close()
