import csv

employees = []
with open("employees.csv", 'r', newline='') as emp_file:
    csv_reader = csv.reader(emp_file)
    for row in csv_reader:
        employees.append(row)
    # employees = [row for row in csv_reader]

print("Header: ", employees[0][0], employees[0][1])
for row in employees[1:]:
    print(row[0], row[1])
