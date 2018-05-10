from random import randint, choice
from math import gcd


def get_index(a):
    if a == ' ':
        return 0
    return ord(a) - 64


def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False
    for i in range(3, int(num // 2) + 1, 2):
        if num % i == 0:
            return False
    return True


# Extended Euclid Algorithm
def eea(a, b):
    if b == 0:
        return 1, 0
    q, r = (a // b, a % b)
    s, t = eea(b, r)
    return t, s - (q * t)


# Find the multiplicative inverse of x (mod y)
def find_inverse(x, y):
    inv = eea(x, y)[0]
    if inv < 1:
        inv += y  # we only want positive values
    return inv


def generate_keys():
    p_nr, q_nr = 0, 0
    while q_nr == 0:
        primes = []
        while len(primes) < 2:
            start_seed = randint(0, 9999)  # primes of approximately same size
            for i in range(start_seed - 20, start_seed + 20):
                if is_prime(i):
                    primes.append(i)

        p_nr = choice(primes)
        q_nr = choice(primes)  # rsa with k = 2 and l = 3
        if (q_nr * p_nr) < 27 ** 2 or (q_nr * p_nr) > 27 ** 3 or q_nr == p_nr:
            p_nr, q_nr = 0, 0

    n_nr = p_nr * q_nr
    fi_n = (p_nr - 1) * (q_nr - 1)

    choices = []
    for i in range(3, fi_n, 2):
        if gcd(i, fi_n) == 1:
            choices.append(i)

    # choices = [i for i in range(3, fi_n, 2) if gcd(i, fi_n) == 1]
    e_exp = choice(choices)

    public_key = (n_nr, e_exp)
    private_key = (n_nr, find_inverse(e_exp, fi_n))

    return (public_key, private_key)


def encrypt(plain, public_key):
    alpha = [
        ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    if len(plain) % 2:
        plain += ' '
    text = str.upper(plain)
    ltx = len(text)
    n_nr = int(public_key[0])
    e_exp = int(public_key[1])

    numerical = []
    for i in range(0, ltx, 2):
        numerical.append(str(get_index(text[i]) * 27 + get_index(text[i + 1])))

    encrypted_numerical = []
    for block in numerical:
        encrypted_numerical.append(int(block) ** e_exp % n_nr)

    encrypted = ''
    for i in encrypted_numerical:
        encrypted += alpha[i // 27 ** 2 % 27]
        encrypted += alpha[i // 27 % 27]
        encrypted += alpha[i % 27]

    return encrypted


def decrypt(cipher, private_key):
    alpha = [
        ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    text = str.upper(cipher)
    ltx = len(text)
    n_nr = int(private_key[0])
    d_exp = int(private_key[1])

    numerical = []
    for i in range(0, ltx, 3):
        numerical.append(str(
            get_index(text[i]) * 27 ** 2 + get_index(text[i + 1]) * 27 + get_index(text[i + 2])))

    decrypted_numerical = []
    for block in numerical:
        decrypted_numerical.append(int(block) ** d_exp % n_nr)

    decrypted = ''
    for i in decrypted_numerical:
        decrypted += alpha[i // 27 % 27]
        decrypted += alpha[i % 27]

    return decrypted
