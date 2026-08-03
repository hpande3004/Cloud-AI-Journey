# Print all key value pairs
def dict(data):
    for key, value in data.items():
        print(key, ":", value)
bb = {"HP": 4,
      "SP": 6,
      "AAP": 8,
      "RP": 3,
      "AP": 1}
result = dict(bb)
print(result)

#Search for a key
def search(data, key):
    if key in data:
        print("Key present")
    else:
        print("Key absent")
student = {
    "Name": "Harshit",
    "Age": 22,
    "City": "Pune"
}
search (student, "Age")
search (student, "Color")

#Count values greater than 80
def count(data):
    count = 0
    for x in data.values():
        if x > 80:
            count += 1
    return count
student = {"RR" : 90,
           "RW" : 79,
           "RV" : 83,
           "RU" : 95,
           "RT" : 64,
           "SS" : 90}
result = count(student)
print(result)

#Return the topper
def topper(marks): 
    highest_marks = 0
    topper_name = ""
    for i in marks:
        if marks[i] > highest_marks:
            highest_marks = marks[i]
            topper_name = i
    return topper_name
students= {"Rahul": 90,
           "Sachin": 84,
           "Yuvraj": 96,
           "Virat": 88,
           "Dhoni": 79}
result = topper(students)
print(result)