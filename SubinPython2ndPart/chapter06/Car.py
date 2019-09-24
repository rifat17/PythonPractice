class Vehicle:
    """Base Class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")


class Car(Vehicle):
    """Car Class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red")

    c.drive()
    c.brake()
    c.change_gear("P")
