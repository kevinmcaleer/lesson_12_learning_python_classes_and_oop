from diesel import Diesel
from electric import Electric
class Car(Diesel,Electric):
    pass

c = Car()

print(c.can_charge)
print(c.cc)

