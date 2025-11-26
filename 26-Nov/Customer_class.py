class Customer:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def check_loyal(self):
        if self.age >25:
            return "Loyalty Program Eligible"
        else:
            return "Loyalty Program Not Eligible"

    def display(self):
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.check_loyal())

