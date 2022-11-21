# from sda.intermediate.check_prime import is_prime
#
#
# class PrimeIterator:
#     # Iterator that allows you to iterate over n primes
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#         elif is_prime(self.number):
#             self.generated_numbers += 1
#             return self.number
#         return self.__next__()
#
# import sys
# prime_iter = PrimeIterator(5)
# for elem in prime_iter:
#     print(elem)
#
# print()

import re
sum = 0
pattern='back'
if re.match(pattern, 'backup.txt'):
    sum += 1
if re.match(pattern, 'text.back'):
    sum += 2
if re.search(pattern, 'backup.txt'):
    sum += 4
if re.search(pattern, 'text.back'):
    sum += 8
print(sum)

