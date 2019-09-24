class Vehicle:
    """Base Class for All vehicles"""

    def __init__(self, name, manufacturer, color):
        print("Creating vehicle..")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Car(Vehicle):
    """Car Class"""

    def __init__(self, name, manufacturer, color, year=2017):
        print("Creating a Car..")
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 4


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2018)
    print(c.name, c.year, c.wheels)
