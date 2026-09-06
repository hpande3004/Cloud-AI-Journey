'''Dunder Methods'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return "Student Name: {}, Marks: {}".format(self.name, self.marks)
    
student = Student("John", 85)
print(student)

#-------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        return len(self.name)
    
student = Student("Harshit")
print(len(student))