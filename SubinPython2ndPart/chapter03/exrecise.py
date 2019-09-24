class Car:
    def __init__(self, name, manufac, color, year, cc ):
        self.name = name
        self.manufacturer = manufac
        self.color = color
        self.year = year
        self.cc = cc

    def Start(self):
        print("Engine Start :) ")

    def Break(self):
        print("Break Pressed")

    def Drive(self):
        print("Start to Drive")

    def Turn(self, on=None, angle=None):
        print("Makes a Turn {} degree {}".format(angle,on))

    
    def ChangeGear(self):
        print("Gear Changed")



myCar = Car("Corolla","MyCompany", "Gray" , "2025", "600")

print(dir(Car))

myCar.Start()
myCar.Drive()
myCar.Break()
myCar.Turn('Left', '15')
# myCar.Turn()
myCar.ChangeGear()

