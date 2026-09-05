class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")

student = Student("Harshit", 85)

print(student.marks)

student.marks = 95
print(student.marks)

student.marks = 150
print(student.marks)
