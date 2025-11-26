class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,name,price):
        self.items.append((name,price))
        print(name, "added to cart")

    def remove_item(self,name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(name, "removed from cart")
                return
        print(name, "not in cart")

    def total_cost(self):
        total=0
        for item in self.items:
            total += item[1]
        return total

    def apply_discount(self,percent):
        total=self.total_cost()
        discount_amount=total * (percent/100)
        final_price =total-discount_amount
        return final_price

    def display_items(self):
        if not self.items:
            print("No items to display")
            return

        print("Items in cart:")
        for name, price in self.items:
            print(name,"-", price)

cart=ShoppingCart()

cart.add_item("Laptop",90000)
cart.add_item("Keyboard",1500)
cart.add_item("Mouse",2000)

print()
cart.display_items()
print()

print("total cost:", cart.total_cost())
print("Final price after 10% discount:", cart.apply_discount(10))

print()
cart.remove_item("Mouse")
cart.display_items()