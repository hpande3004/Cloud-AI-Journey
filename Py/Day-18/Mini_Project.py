'''Mini Project - Student JSON Database
This project allows you to manage a student database using JSON files. 
You can add new students and view existing students in the database'''

import json

FILE_NAME = "student.json"


# Add a new student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

    print("Student added successfully! ✅")


# Display all students
def show_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    if len(students) == 0:
        print("No students found.")
    else:
        print("\n----- Student Database -----")

        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("----------------------------")


# Main menu
while True:

    print("\n===== STUDENT JSON DATABASE =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Program closed. 👋")
        break

    else:
        print("Invalid choice. Please try again.")