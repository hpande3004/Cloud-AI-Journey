'''Nested JSON'''
student = {
    "name" : "Harry",
    "age" : 22,
    "address" : {
        "city" : "Pune",
        "state" : "Maharashtra"
    }
}
print(student["address"]["state"])

student = {
    "name" : "harshit",
    "age" : 22,
    "skills" : ["Python", "AWS", "Azure"]
}
print(student["skills"][1])