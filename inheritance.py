class Bird:
    def __init__(self,type):
        self.type=type
        print(f"It is a {self.type} Bird")
        print("Constructor is called")

    def hasFeather(self):
        print("Bird has feather")

    def layEgg(self):
        print("Bird lays eggs")

class Parrot(Bird):
    def __init__(self,color,type):
        super().__init__(type)
        self.color=color

    def showColor(self):
        print(f"Bird is of {self.color} color")

class Ostrich(Bird):
    def noFly(self):
        print("Bird has feathers but can not fly!!")

par=Parrot("green","terrestrial")
ost=Ostrich("terrestrial")

par.hasFeather()
par.layEgg()
par.showColor()

ost.hasFeather()
ost.layEgg()
ost.noFly()

