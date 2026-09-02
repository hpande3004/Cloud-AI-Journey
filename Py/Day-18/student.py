# Writing JSON data to a file

import json
import os

student = {
    "name": "Harshit",
    "age": 22,
    "marks": 85
}

print("Python is looking for the file here:")
print(os.path.abspath("data.json"))

with open("data.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")

# ---------------------------------------------

# Reading JSON data from a file

import json

with open("data.json", "r") as file:
    student = json.load(file)

print(student)