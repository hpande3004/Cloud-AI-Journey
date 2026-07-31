''' Level 1 tasks on Day-2
1. Print numbers from 1 to 20 using a for loop'''

for i in range (1, 21):
    print(i)

'''2. Print all even numbers from 1 to 100 using a for loop'''
for i in range (1, 101):
    if i % 2 == 0 :
        print(i)

'''3. Create a multiplication table of a given number using a for loop.'''
i = int(input("Enter a number: "))
for j in range (1, 11):
    print(i, "x", j, "=", i*j)

'''4. Calc sum of numbers from 1 to N'''
n = int(input("Enter a number: "))
sum = 0
for i in range (1, n+1):
    sum += i
print("The sum of numbers from 1 to", n, "is:", sum)


'''5. Reverse Counting'''
c = int(input("Enter a number: "))
while c > 0:
    print(c)
    c -= 1
else:
    print("Blast Off!")