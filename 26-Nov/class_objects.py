class Student:
    pass

s3= Student() #new object being created, memory being allocated
s4= Student()

######################################################################
class Student:
    def __init__(self,name,age): #Constructor - self isn't a parameter, name and age are
        self.name=name  #self is used in place of this
        self.age=age #self is an object of the current class


s1 = Student("Ankur",22)
s2 = Student("Messi",38)

print(s1.name,s1.age)


