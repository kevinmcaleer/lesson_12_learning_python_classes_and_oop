from animal import Animal, Leg

archie = Animal("Archie")

print(archie.name)

leg = Leg()

leg.name = "front-left"
leg2 = Leg()
leg2.name = "back-left"
archie.legs.append(leg)
archie.legs.append(leg2)
archie.show()