class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks  # marks is a number (0–100)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}")

s1 = Student(101, "Riya", 88)
s2 = Student(102, "Kabir", 35)

s1.display()
s2.display()
