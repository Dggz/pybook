import csv
from sys import argv
from datetime import datetime, date, timedelta

file_name = "expenses" # argv[1]


with open(file_name, 'r') as inp:
    lines = inp.readlines()
    prices = (row for row in csv.reader(lines) if len(row) == 2)
    expenses = {domain: int(amount) for domain, amount in prices}

start_money = 2500 # int(input("How much money do you have?: "))  # 2000
print()

[print(dom, amount) for dom, amount in expenses.items()]
expense_amount = sum(expenses.values())
left = start_money - expense_amount

today = datetime.now()
if (today.year == 2023 and today.month == 8 and today.day < 14):
    final_date = datetime(today.year, datetime.now().month + 1, 15)
elif today.day < 14:
    final_date = datetime(today.year, datetime.now().month, 15)
else:
    final_date = datetime(today.year, datetime.now().month + 1, 15)
remaining_days = (final_date - today).days + 1

daily_budget = int(left / remaining_days)
if .8 * daily_budget > 30:
    print("\nBudget is over 30/day.\n"
          "This will result in {} in savings".format(
              left - 30 * remaining_days)
          )
print("\nRemaining days:", remaining_days)
print("\nExpenses:", int(expense_amount))
print("Money left:", int(left))
print("Daily budget:", daily_budget)
print(
    "Daily budget to save up 20% ({}):".format(int(.2 * left)),
    int(.8 * daily_budget)
)
