class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item_name, price):
        self.items[item_name] = price
        print(f"Added {item_name} for ₹{price}")

    def remove(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Removed {item_name}")
        else:
            print(f"{item_name} not found in cart")

    def total(self):
        return sum(self.items.values())

    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            print("Invalid discount percentage")
            return self.total()
        discount_amount = self.total() * (percent / 100)
        return self.total() - discount_amount
cart = ShoppingCart()
cart.add("Mouse", 799)
cart.add("Keyboard", 1599)

print("Total:", cart.total())  # 2398
print("After 10% discount:", cart.apply_discount(10))  # 2158.2

cart.remove("Mouse")
print("Total after removal:", cart.total())
