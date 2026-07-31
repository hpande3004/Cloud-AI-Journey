'''Level 2 tasks on Day 2
Q6. Count vowels in a string'''

txt = input("Enter your word: ")
vowels = "aeiouAEIOU"
vwl_count = 0
for x in txt:
    if x in vowels:
        vwl_count += 1
print("The number of vowels in the string are: ", vwl_count)

'''7. Largest number among 5 numbers entered by user'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
largest = num1
for x in (num1, num2, num3, num4, num5):
    if x > largest:
        largest = x
print(largest, "is the largest")

# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print ('*'*i)
        
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print("*"*i)

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1, i+1):
        print(j, end="")
    print()
