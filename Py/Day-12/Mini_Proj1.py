'''Mini Project 1 - Student Management Analysis using OOPs'''

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)

    def is_passed(self):
        return self.marks >= 40

class Student_Management:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added")

    def display_student(self):
        if not self.students:
            print("No students found")
            return
        for student in self.students:
            student.display()
            print("-" * 20)

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student

        return None

    def delete_student(self, name):
        student = self.find_student(name)

        if student:
            self.students.remove(student)
            print("Student deleted Successfully!")
        else:
            print("Student not found")

manager = Student_Management()

while True:

    print("\n======Student Management======")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Find Student")
    print("4. Delete Student")
    print("Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Student name: ")
        marks = float(input("Enter marks obtained: "))

        student = Student(name, marks)
        manager.add_student(student)

    elif choice == "2":

        manager.display_student()

    elif choice == "3":

        name = input("Enter student name: ")
        student = manager.find_student(name)

    elif choice == "4":

        manager.delete_student()

    elif choice == "5":
        print("Thanks! Have a good day")
        break

    else:
        print("Invalid choice")