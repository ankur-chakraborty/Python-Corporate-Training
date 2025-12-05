import csv

employees = [
    {"id": i, "name": f"Employee{i}", "department": "Dept" + str((i % 5) + 1), "salary": 40000 + i * 1000}
    for i in range(1, 21)
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "department", "salary"])
    writer.writeheader()
    writer.writerows(employees)

print("CSV file 'employees.csv' created successfully!")


#read from a csv file


employee_list = []
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employee_list.append(row)

print("Employees read from CSV:")
for emp in employee_list:
    print(emp)
