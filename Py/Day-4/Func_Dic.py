# '''Functions and Dictionaries
# Q1. Create dict to return the topper's marks'''
def topper(marks):
    topper_name = ""
    highest_marks = 0
    for student in marks:
        if marks[student] > highest_marks:
            highest_marks = marks[student]
            topper_name = student
    return topper_name
students = {
    "Rahul": 90,
    "Amit": 84,
    "Priya": 96,
    "Riya": 88,
    "Karan": 79
}
result = topper(students)
print("Topper: ", result)

# #Q2. Print every value
def pren(data):
    for key, value in data.items():
        print(key, ":", value)
student = {
    "Name": "Harshit",
    "Age": 22,
    "City": "Pune"
}
pren(student)

#Q3. Search whether a key exists
def search_key(data, key):

    if key in data:
        print("Key Found")
    else:
        print("Key Not Found")


student = {
    "Name": "Harshit",
    "Age": 22,
    "City": "Pune"
}

search_key(student, "Age")
search_key(student, "Salary")

#Q4. Count students scoring more than 80
def classroom(marks):
    count = 0
    for x in marks.values():                        #.values() returns only the values of the dict
        if x > 80:
            count += 1
    return count
students = {
    "Rahul": 90,
    "Amit": 72,
    "Priya": 96,
    "Riya": 81,
    "Karan": 65
}
result = classroom(students)
print(result)