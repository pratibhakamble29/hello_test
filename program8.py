 
class car:
    def addNewcar(self):
        self.carname = input("Enter car name :")
        self.colour = input("Enter car colour :")
        self.cost = input("Enter car cost :")

class BMW(car):
    def discribeBMWCar(self):
        print("BMW car move fast")

class Ferrari(car):
    def discribeFerraricar(self):
        print("Ferrari is a sport car move very fast")

b1 = BMW()
b1.addNewcar
b1.discribeBMWCar

f1 = Ferrari()
f1.addNewcar
f1.discribeFerraricar

