class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand", self.brand)
        print("Model",self.model)
        print("Price",self.price)

#Creating three Car objects

car1=Car("Volkswagen", "Virtus", "19 Lakhs")
car2=Car("Tata", "Safari", "26 Lakhs")
car3=Car("Hyundai","i20","8.5 Lakhs")

car1.display()
car2.display()
car3.display()