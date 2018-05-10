from random import randint, choice
from math import gcd
from collections import defaultdict


def check_space(a):
    if a == ' ':
        return 0
    if ord(a) - 64 < 0 or ord(a) - 64 > 26 or a == '@':
        return -(27 ** 3)
    return ord(a) - 64


def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
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
            primes = [
                i for i in range(start_seed - 100, start_seed + 100)
                if is_prime(i)
            ]

        p_nr = choice(primes)
        q_nr = choice(primes)  # rsa with k = 2 and l = 3
        if (q_nr * p_nr) < 27 ** 2 or (q_nr * p_nr) > 27 ** 3 or q_nr == p_nr:
            p_nr, q_nr = 0, 0

    n_nr = p_nr * q_nr
    fi_n = (p_nr - 1) * (q_nr - 1)

    choices = [i for i in range(3, fi_n, 2) if gcd(i, fi_n) == 1]
    e_exp = choice(choices)

    public_key = (n_nr, e_exp)
    private_key = (n_nr, find_inverse(e_exp, fi_n))

    return public_key, private_key


def encrypt(plain, public_key):
    alpha = defaultdict(int)
    alpha[0] = ' '
    for i in range(65, 91):
        alpha[i - 64] = chr(i)

    if len(plain) % 2:
        plain += ' '
    text = str.upper(plain)
    ltx = len(text)
    n_nr, e_exp = int(public_key[0]), int(public_key[1])

    numerical = []
    for i in range(0, ltx, 2):
        numerical.append(str(
            check_space(text[i]) * 27 + check_space(text[i + 1])))

    for i in numerical:
        if int(i) < 0:
            return 'Unsupported character for encryption'
    encrypted_numerical = [pow(int(block), e_exp, n_nr) for block in numerical]
    encrypted = ''.join([
        ''.join((alpha[i // 27 ** 2 % 27], alpha[i // 27 % 27], alpha[i % 27]))
        for i in encrypted_numerical])
    return encrypted.replace(' ', '_')


def decrypt(cipher, private_key):
    alpha = defaultdict(int)
    alpha[0] = ' '
    for i in range(65, 91):
        alpha[i - 64] = chr(i)

    text = str.upper(cipher.replace('_', ' '))
    ltx = len(text)
    n_nr, d_exp = int(private_key[0]), int(private_key[1])

    numerical = []
    for i in range(0, ltx, 3):
        numerical.append(str(
            check_space(text[i]) * 27 ** 2
            + check_space(text[i + 1]) * 27
            + check_space(text[i + 2])))

    for i in numerical:
        if int(i) < 0:
            return 'Unsupported character for decryption'
    decrypted_numerical = [pow(int(block), d_exp, n_nr) for block in numerical]
    decrypted = ''.join([''.join(
        (alpha[i // 27 % 27], alpha[i % 27])) for i in decrypted_numerical])
    return decrypted.lower()
