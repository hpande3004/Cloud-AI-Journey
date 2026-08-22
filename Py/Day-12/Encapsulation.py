class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def getage(self):
        return self.__age

    def set_age(self, age):
        if age >0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tom", 27)
print(p1.getage())

p1.set_age(24)
print(p1.getage())