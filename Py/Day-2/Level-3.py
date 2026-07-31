'''Level 3 tasks on Day 2
11. Create func that returns square of a number'''
def square():
    num = int(input("Enter the number: "))
    print("Square of entered number: ", num**2)
square()

# 12. Create func to check if num is even or odd
def myfunc():
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
myfunc()

# 13. Create func to count upper and lower case letters in a string
def myfunc(txt):
    upper_count = 0
    lower_count = 0
    for char in txt:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return{"Uppercase": upper_count, "Lowercase": lower_count}

print(myfunc("Hello Wrold 1@M"))