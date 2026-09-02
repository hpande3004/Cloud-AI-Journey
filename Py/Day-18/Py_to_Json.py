students = [
    {
        "name": "Rahul",
        "marks": 80
    },
    {
        "name": "Priya",
        "marks": 92
    },
    {
        "name": "Amit",
        "marks": 75
    }
]

import json
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)