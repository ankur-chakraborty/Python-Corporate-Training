class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}, Price: ₹{self.price}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def display(self):
        print(f"Electronic Product: {self.name}, Price: ₹{self.price}, Warranty: {self.warranty_years} years")

p1 = Product("Notebook", 50)
p2 = ElectronicProduct("Laptop", 70000, 2)

p1.display()
p2.display()
