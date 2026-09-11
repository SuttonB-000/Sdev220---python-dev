class Vehicle:
    def __init__(self):
        self.type = type

class Automobile(Vehicle):
    def __init__(self):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

print('|___Car Qualities____|')

Automobile.year = input("Year... ")
Automobile.make = input("Make... ")
Automobile.model = input("Model... ")
Automobile.doors = input('Doors... ')
Automobile.roof = input('Roof style... ')

my_car = [Automobile.year, Automobile.make, Automobile.model, Automobile.doors, Automobile.roof]

for i in my_car:
    print(i)
