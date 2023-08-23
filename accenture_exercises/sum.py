class Vehical:
    def __init__(self, name, color):
        self._name = name
        self._color = color
    
    def _drive(self):
        print("I don't drive")

    def _my_color(self):
        print("my color is ", self._color)


class Car(Vehical):
    def __init__(self, name, color, lights):
        super().__init__(name, color)
        self._lights = lights

    def _drive(self):
        print("other processing ")
        print("Car is driven")


class Bus(Vehical):
    def _drive(self):
        print("Bus is driven")

class Truck(Vehical):
    def _drive(self):
        print("Truck is driven")

def process(v: Vehical):
    v._drive()
    v._my_color()

v = Vehical("V1", "R")
c = Car("C1", "B", "4")
b = Bus("B1", "D")
t = Truck("T1", "P")

process(c)
