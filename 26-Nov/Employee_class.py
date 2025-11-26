class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


e1 = Employee(101, "Ankur", "DET", 35000)
e2 = Employee(102, "Dips", "AI", 40000)

e1.display()
e2.display()

