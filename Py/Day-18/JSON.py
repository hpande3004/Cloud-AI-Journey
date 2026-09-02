'''JSON'''
#Py to JSON
import json
Person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(Person)
print(json_string)
print(type(json_string))

#JSON to Py
import json
Dict = '{"name": "HH", "age": 25, "city": "LA"}'
py_dict = json.loads(Dict)
print(py_dict)
print(type(py_dict))