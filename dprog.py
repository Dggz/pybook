import time
from functools import wraps


def timethis(func):
    """Decorator that reports the execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@timethis
def call_fib(n):
    return fib(n)


def pfib(n):
    if n <= 2:
        print('fib({})'.format(n))
        return 1
    else:
        print('fib({}): fib({}) + fib({})'.format(n, n-1, n-2))
        return pfib(n-1) + pfib(n-2)


def dfib(n):
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2])
    return fib_values[n]


@timethis
def call_df(n):
    return dfib(n)


def memoize(f):
    cache = {}

    def memoized_function(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    memoized_function.cache = cache
    return memoized_function


@memoize
def mfib(n):
    if n <= 2:
        return 1
    else:
        return mfib(n-1) + mfib(n-2)


def coin_change(cents_needed, coin_values):
    min_coins = [[0] * (cents_needed + 1)] * len(coin_values)
    import ipdb; ipdb.set_trace()
    min_coins[0] = range(cents_needed + 1)
    import ipdb; ipdb.set_trace()

    for i in range(1, len(coin_values)):
        for j in range(0, cents_needed + 1):
            if j < coin_values[i]:
                min_coins[i][j] = min_coins[i-1][j]
        else:
            min_coins[i][j] = min(
                min_coins[i-1][j], 1 + min_coins[i][j - coin_values[i]])

    # import ipdb; ipdb.set_trace()
    return min_coins[-1][-1]


print(coin_change(150, [1, 5, 10, 50]))
