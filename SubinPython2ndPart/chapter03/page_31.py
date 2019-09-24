class Car:
    # name = ""
    # color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("name : ",self.name)
        print("color : ",self.color)
        print("Starting the Engine")


myCar = Car("Corolla", "white")

# print(myCar.name)
# print(myCar.color)
# myCar.start()

# Car.start(myCar)


car1 = Car("Corolla", "White")
car1.start()
car2 = Car("Premio" , "Black")
car2.start()
car3 = Car("Allion", "Blue")
car3.start()
