
class Vehicle:
    def __init__(self, name):
        self.name = name

    def max_speed(self):
        return "Speed not defined"


class Car(Vehicle):
    def max_speed(self):
        return "Car max speed: 220 km/h"


class Bike(Vehicle):
    def max_speed(self):
        return "Bike max speed: 160 km/h"


# Example usage
v = Vehicle("Generic Vehicle")
c = Car("Honda City")
b = Bike("Yamaha R15")

print(v.max_speed())
print(c.max_speed())
print(b.max_speed())
