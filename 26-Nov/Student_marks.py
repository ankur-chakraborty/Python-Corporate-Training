class Student:
    def __init__(self, name, m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3
    def percentage(self):
        return (self.total()/300)*100
    def grades(self):
        if self.percentage()>=90:
            return "A"
        if self.percentage()>80:
            return "B"
        if self.percentage()>70:
            return "C"
        if self.percentage()>60:
            return "D"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grades:", self.grades())


s1=Student("Ankur",85,90,95)
s1.display()