'''Level 3 Tasks Day 3'''
#DICTIONARIES
# 10. Store marks of 5 students in a dict and print the marks of topper student

marks = { 'Shivam': 85,
         'Harshit': 96,
         'Amit': 70,
         'Rohit': 90,
         'Saurabh': 80}
top = max(marks, key=marks.get)
print("Topper student marks is:", marks[top])

#11. Count the frequency of every character in a string input by user
i = input("Enter a string: ")
dict = {}
for j in i:
    if j in dict:
        dict[j] += 1
    else:
        dict[j] = 1
print(dict)

#12. Create a dictionary of 5 countries and their capitals. Ask user to input a country and print the capital of that country.
capitals = { "USA" : "Washington D.C",
             "India" : "New Delhi", 
              "China" : "Beijing",
              "Russia" : "Moscow"}
country = input("Enter a country: ")
if country in capitals:
    print("The capital of", country, "is", capitals[country])
else:
    print("Country not found.")

