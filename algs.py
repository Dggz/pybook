
def read_file():
    with open('alginput') as alginp:
        lines = alginp.readlines()
    return lines


def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False
    for i in range(3, int(num // 2) + 1, 2):
        if num % i == 0:
            return False
    return True


def r1_1():
    lines = read_file()
    n = int(lines[0])
    nrs = map(int, lines[1].split())
    freq =  [0] * 100
    for nr in nrs:
        freq[nr] += 1

    print([i for i in range(100) if freq[i]!=0])

def r2_1():
    lines = read_file()
    nrs = map(int, ''.join(lines[3:-1]).split())
    maxx = max(nrs)
    output, prime = 0, maxx
    while output == 0:
        if is_prime(prime):
            output = prime
        prime += 1
    print(output)

def main():
    # r1_1()
    r2_1()

main()
