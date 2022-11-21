# import json
#
# students = [
#     {
#         'name': "John",
#         'surname': "Smith",
#         'score': 20
#     },
#     {
#         'name': "Kevin",
#         'surname': "Scoot",
#         'score': 17
#     }
# ]
#
# with open("students.json", 'w') as out_file:
#     json.dump(students, out_file, indent=2)
#
# # with open("students.json", 'r') as in_file:
# #     studs = json.load(in_file)
#
# exit(0)

from datetime import datetime
import time
from functools import wraps

def disable_at_night(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
    return wrapper


@disable_at_night
def say_something():
    print("Hello world")


# say_something()



def timethis(func):
    """Decorator that reports the execution time."""
    """annotations and stuff __name__ __doc__ __annotations__"""
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n: int):
    """Counts down"""
    while n > 0:
            n -= 1


@timethis
def sum_(number: int):
    return sum(range(number))


# countdown(1000)
#
#
# sum_(500)


def run_only_between(start=7, end=22):
    # a decorator that only calls a decorated function at certain times

    def dec(func):
        # @wraps(func)
        def wrapper():
            if start <= datetime.now().hour < end:
                func()

        return wrapper

    return dec


@run_only_between(10, 15)
def say_something():
    print("Hello world")


# say_something.__wrapped__()
say_something()
