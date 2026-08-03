'''MINI - PROJECT'''

#Students Marks Analyzer
# Rahul - 90, Amit - 75, Priya - 96, Riya - 81, Karan - 68

students = {"Rahul" : 90, "Amit" : 75, "Priya" : 96, "Riya" : 81, "Karan" : 68}

def show_student(data):
    print("\n------Student Data-------")
    for key, value in data.items():
        print(key, ":", value)

def show_topper(data):
    topper_name = ""
    highest_marks = 0

    for students in data:
        if data[students] > highest_marks:
            highest_marks = data[students]
            topper_name = students

    print("\nTopper: ", topper_name)
    print("Marks: ", highest_marks)

def average_marks(data):
    total = 0

    for x in data.values():
        total += x

    average = total / len(data)

    print("\nAverage marks: ", average)

def count_above_80(data):
    count = 0

    for y in data.values():
        if y > 80:
            count += 1

    print("\nStudents above 80: ", count)

def search_student(data):
    name = input("Enter student name: ")

    if name in data:
        print("Student present")
    else:
        print("Student absent")

while True:
    print("\n========Student Management System==========")
    print("1. Show Students")
    print("2. Show Topper")
    print("3. Show Average Marks")
    print("4. Count Students above 80")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_student(students)
    elif choice == "2":
        show_topper(students)
    elif choice == "3":
        average_marks(students)
    elif choice == "4":
        count_above_80(students)
    elif choice == "5":
        search_student(students)
    elif choice == "6":
        print("Thank you")
        break
    else:
        print("Invalid Choice")