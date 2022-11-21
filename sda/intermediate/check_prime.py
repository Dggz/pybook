import sys
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(number_of_primes):
    primes = []
    i = 2
    while len(primes) < number_of_primes:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

if __name__ == '__main__':
    lst = get_n_primes(1000000)
    print(sys.getsizeof(lst))
    for elem in lst:
        print(elem)
