class Vehicle:
    def __init__(self,typeOfVehicle, wheels, country):
        self.country = country
        self.typeOfVehicle = typeOfVehicle
        self.wheels = wheels

    def display(self):
        print(self.typeOfVehicle, "- Type of vehicle")
        print(self.wheels, "wheel vehicle")
        print(self.country, "is country of Origin")


class Car(Vehicle):
    def __init__(self, nameOfCar, Brand, Transmission, typeOfVehicle, wheels, country):
        super().__init__(typeOfVehicle, wheels, country)
        self.nameOfCar = nameOfCar
        self.Brand = Brand
        self.Transmission = Transmission

    def display(self):
        super().display()
        print(self.nameOfCar, "- Name of car")
        print(self.Brand, "- Brand")
        print(self.Transmission, "- Transmission")


c=Car("Virtus", "Volkswagen", "6-gear manual", "Car",4,"Mexico")
c.display()

