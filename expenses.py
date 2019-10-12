import csv
from sys import argv
from datetime import datetime, date, timedelta

file_name = argv[1]


with open(file_name, 'r') as inp:
    lines = inp.readlines()
    prices = (row for row in csv.reader(lines) if len(row) == 2)
    expenses = {domain: int(amount) for domain, amount in prices}

start_money = int(input("How much money do you have?: "))  # 2000
print()

[print(dom, amount) for dom, amount in expenses.items()]

left = start_money - sum(expenses.values())

today = datetime.now()
final_date = final = datetime(2019, datetime.now().month + 1, 6)
remaining_days = (final_date - today).days + 1
print(remaining_days)

print("\nMoney left:", int(left))
print("Daily budget:", int(left / remaining_days))
print(
    "Daily budget to save up 20% ({}):".format(int(.2 * left)),
    int(.8 * left / remaining_days)
)
