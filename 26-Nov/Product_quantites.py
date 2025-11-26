class Product:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def display(self):
        print("Name:",self.name)
        print("Quantity:",self.quantity)
        print("Price for each:",self.price)
        print("Total Price:",self.price*self.quantity)


prod=Product("Milk",10,28)
prod.display()