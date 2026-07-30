print("Hello, World!")                                          #Basic

name="Harshit"                                                  #Learning Var
age=22
print("My name is", name, "and I am", age, "years old.")        #Print Statement

import sys
print(sys.version)                                              #Checking Python version

if 5>2:
    print("Five is greater than two!")                          #If loop

print("This is a comment"); print("This is not a comment")      #Commenting

print("Hello Sir", end=" ")                                     #End Statement
print("How are you?")

print ("I am", 22, "years old")                                 #Print Statement

x=4
X="Four"
print(x)                                                        #Var reassignment
print(type(x))                                                  #Var type       


y="Harry"                                                       #Global Variable

def myfunc():
    global y                                                    #Global Variable
    y="Harshit"                                                 #Local Variable
    print(y)
myfunc()                                                        #Function
print(y)                                                        #Function

ab=1
cd=3.7
b=float(ab)
c=int(cd)
print(b)                                                        #Data Type Conversion
print(c)

import random   
print(random.randrange(1,10))                                   #Random Number Generation

cars=["Ford", "Volvo", "BMW"]                                   #List
cars.append("Honda")                                            #List Append
print(cars)

student={
    "name": "Harshit",                                          #Dictionary
    "age": 22,
    "course": "Python"
}
print(student["name"])                                         #Dictionary Print

txt="I'll definitely make it one day"
if "one" in txt:
    print("one is present")                                     #if statement
if "two" in txt:
    print("two is present")
else:
    print("Error occured")                                      #If else statement

age=22
txt=f"My name is Harshit, and I am {age} years old."            #f-string
print(txt)

print(input("Enter your name: "))  
name=input()                                                    #Input Statement
print(f"Hello {name}")