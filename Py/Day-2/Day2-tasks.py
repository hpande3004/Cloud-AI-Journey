# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "blueberry"                         #List item modification
# print(fruits)                                   #Lists
# fruits.insert(2, "orange")                      #List item insertion
# print(fruits)                                   #Lists

# cars = tuple(("Ford", "BMW", "Volvo"))          #Tuples
# fruits.extend(cars)                             #Extending a list with a tuple
# print(fruits)                                   #Lists

# fruits.pop(1)
# print(fruits)                                   #Pop op Lists

# city = ["Mumbai", "Pune", "Nagpur"]
# for x in city:
#     print(x)                                    #For loop Lists    

# for i in range(len(city)):
#     print(city[i])                              #For loop with range Lists

# city = [x.lower() for x in city]                #List comprehension
# print(city)

# city = ['Hyderabad' for x in city]
# print(city)                                     #List comprehension

# -------------------------------------------------------
# TUPLE

# t = ("AAA",)
# print(type(t))                                    #Tuple with single value

# tuple1 = ("AAA")
# print(type(tuple1))                                   #Not a tuple its a string

# x = ('A', 'B', 'C', 'D')
# y = list(x)
# y[1] = 'Z'
# x = tuple(y)
# print(x)                                              #Tuple modification

# age = 12
# if age < 13:
#     print("You are a child.")
# elif age < 18:
#     print("You are a teenager.")
# else: 
#     print("You are an adult.")


# i = 1
# while i < 6:
#     print(i)
#     i += 1                          #While Loop
# else:
#     print("i is no longer less than 6") #with else statement


# i = 1
# while i <10:
#     print(i)
#     if i == 5:
#         break
#     i += 1                          #While Loop with break

# i = 0

# while i < 10:
#     i += 1
#     if i != 3:
#         continue
#     print(i)                  #While Loop with continue

# city = ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Surat"]
# for x in city:
#     if x == "Hyderabad":
#         break
#     print(x)                  #For Loop with break

# city = ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Surat"]
# for x in city: 
#     print(x)
#     if x == "Hyderabad":
#         break                  #For Loop with break

city = ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Surat"]
# for x in city:
#     if x == "Hyderabad":
#         continue
#     print(x)                  #For Loop with continue

# for x in city:
#     print(x)
#     if x == "Hyderabad":
#         continue

# for x in range(6):
#     if x == 3: continue
#     print(x)                  #For Loop with continue
# else:
#         print("This is not printed because the loop is terminated with a break statement")      #else in for

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)                                                                            #Nested For Loop

