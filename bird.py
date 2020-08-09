from animal import Animal, Leg

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.has_wings = True
    
    def show(self):
        super().show()
        print("Has Wings")
        print(self.has_wings)

pinky = Bird()

pinky.name = "Pinky"

pinky.show()