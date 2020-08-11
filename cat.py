from animal import Animal
from leg import Leg

class Cat(Animal):
    left_leg = Leg()
    right_leg = Leg()
    name = ""

    def __init__(self, cat_name = None):
        if cat_name is None:
            self.name = "no name"
        else:
            self.name = cat_name

    def show(self):
        print("the cats name is: ")
        print(self.name)
        super().show()
    pass

Salem = Cat("Salem")
Salem.eyes = 1
Salem.show()
