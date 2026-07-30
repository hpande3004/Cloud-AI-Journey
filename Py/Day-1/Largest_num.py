# LARGEST NUMBER CHECKER

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter one more number: "))
if x > y and x > z:
    print(x, "is the greatest number")
elif y > x and y > z:
    print(y, "is the greatest number")
else: 
    print(z, "is the greatest number")