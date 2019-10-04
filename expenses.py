import csv
from sys import argv

file_name = argv[1]


with open(file_name, 'r') as inp:
    lines = inp.readlines()
    prices = (row for row in csv.reader(lines) if len(row) == 2)
    expenses = {domain: int(amount) for domain, amount in prices}

start_money = int(input("How much money do you have?: "))  # 2000
print()

[print(dom, amount) for dom, amount in expenses.items()]

left = start_money - sum(expenses.values())

print("\nDaily budget:", int(left / 31))
print("Daily budget to save up 20%:", int(.8 * left / 31))
