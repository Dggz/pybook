debt = 5500
month_plan = 170 * 3 + 27 + 38 + 234 + 206 + 470 + 18 + 754
total_plan = 750 + 240 + 470 + 410 + 465 + 185 + 130 + 510 * 3

out_of_plan = debt - total_plan

ppmonth = month_plan + out_of_plan

next_debt = debt - ppmonth


print('\nThis month: ', ppmonth)
print('\nNon-plan: ', out_of_plan)
print('Month plan: ', month_plan, 'Total plan: ', total_plan)
print('Total debt after current month: ', next_debt)