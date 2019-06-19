
from sys import argv

file_name = argv[1]

with open(file_name, 'r') as inp:
    debt, month_plan, total_plan, known_monthly = map(eval, inp.readline().split(','))


# print('\n\n', month_plan, '\n\n')
out_of_plan = debt - total_plan

ppmonth = month_plan + out_of_plan if not known_monthly else known_monthly
if out_of_plan < 0:
    ppmonth -= out_of_plan

next_debt = debt - ppmonth

# import ipdb; ipdb.set_trace()

print('\nMonth payment: ', ppmonth)
print('\nNon-plan: ', out_of_plan)
print('Month plan: ', month_plan, 'Total plan: ', total_plan)
print('Total debt after computed month: ', next_debt)
