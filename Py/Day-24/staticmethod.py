'''static method'''
#Normal
class Student:
    def show(self):
        print("This is normal method")

#Static
class Student:
    @staticmethod
    def show():
        print("This is static method")