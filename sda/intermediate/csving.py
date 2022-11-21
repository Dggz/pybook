import csv

employees = [
    ['employee',     'salary'],
    ['John Smith',     '2500'],
    ['Jenny Scoot',     '7500'],
    ['Kate Noris',     '10000'],
]

with open('employees.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(employees[0])
    for emp in employees[1:]:
        # if int(emp[1]) > 3000:
        csv_writer.writerow(emp)
    # csv_writer.writerows(employees)
