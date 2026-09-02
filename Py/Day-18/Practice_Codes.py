#Mission 1: Convert a Python object into a JSON string
import json
person = {
    "name" : "harshit",
    "age" : 22,
    "city" : "Pune"
}
json_str = json.dumps(person)
print(json_str)
print(type(json_str))

#Mission 2: Convert a JSON string into a Python object
import json
json_data = '{"name" : "rahul", "age" : 26, "city" : "Mumbai"}'
py_obj = json.loads(json_data)
print(py_obj)
print(type(py_obj))

#Mission 3: Create a list of 3 employees and save them in a JSON file
import json
employees = [
    {
        "name": "Rahul",
        "emp_id": 102,
        "city": "Mumbai"
    },
    {
        "name": "Priya",
        "emp_id": 104,
        "city": "Pune"
    },
    {
        "name": "Amit",
        "emp_id": 106,
        "city": "Delhi"
    }
]
with open("employees.json", "w") as file:
    json.dump(employees, file, indent = 4)

#Mission 4: Read the JSON file and print the employee names
import json
with open("employees.json", "r")as file:
    employees = json.load(file)
print(employees)

#Mission 5: Nested JSON
import json
company = {
    "name": "TechCorp",
    "location": {
        "city": "Pune",
        "country": "India"
    },
    "employees": [
        {
            "name": "Rahul",
            "role": "Developer"
        },
        {
            "name": "Priya",
            "role": "Cloud Engineer"
        }
    ]
}
with open("company.json", "w") as file:
    json.dump(company, file, indent = 4)

import json
with open("company.json", "r") as file:
    company = json.load(file)
print("City : " + company["location"]["city"])
print("Country : " + company["location"]["country"])
print("Employee 1: " + company["employees"][0]["name"] + " - " + company["employees"][0]["role"])
print("Employee 2: " + company["employees"][1]["name"] + " - " + company["employees"][1]["role"])