class Bird:
    def hasFeather(self):
        print("Bird has feather")

    def layEgg(self):
        print("Bird lays eggs")

class Parrot(Bird):
    def color(self):
        print("Bird is of green color")

class Ostrich(Bird):
    def noFly(self):
        print("Bird has feathers but can not fly!!")

par=Parrot()
ost=Ostrich()

par.hasFeather()
par.layEgg()
par.color()

ost.hasFeather()
ost.layEgg()
ost.noFly()

