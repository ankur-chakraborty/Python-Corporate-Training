class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

e = Employee("Ankur", 101)
print(e.name, e.emp_id)