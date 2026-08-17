class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Harry", "Dicosta")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("The name is", self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("John", "Cena")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print("The name is", self.first, self.last)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mic", "Tyson", 2021)
print(x.graduationyear)


# Code Challenge W3Sc
class Animal:
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print(self.name)
  
class Dog(Animal):
  pass

d1 = Dog("Rex")
d1.speak()
