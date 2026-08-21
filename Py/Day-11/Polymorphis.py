class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", 777)

for x in (car1, boat1, plane1):
    x.move()


class Cat:
  def sound(self):
    print("Meow")

class Fox:
  def sound(self):
    print("Wa-pa-pa-pa-pa-pow!")

c1 = Cat()
f1 = Fox()

for animal in (c1, f1):
  animal.sound()