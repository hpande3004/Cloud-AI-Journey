'''Practice Codes'''
#1:Create a lambda that takes a number and returns its cube
num = [23,56,64,59]
cube = list(filter(lambda x: x**3, num))
print(cube)

#2: Create a lambda that takes two numbers and returns the larger number
large = lambda x, y: x if x > y else y
print(large(14,23))
print(large(90,88))

#3: Use map() + lambda to divide every number by 2.
numbers = [2,4,6,8,10]
div = map(lambda x: x/2, numbers)
print(list(div))

#4: Use filter() to keep numbers greater than 15.
numbers = [12, 5, 8, 21, 30, 17, 40]
gtf = filter(lambda x: x > 15, numbers)
print(list(gtf))

#5: Keep only even numbers and square them.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, even)
print(list(squared)) 

#6: Use reduce() to calculate their sum.
from functools import reduce
numbers = [5, 10, 15, 20]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

#7: Mini Challenge
numbers = [3, 7, 12, 15, 20, 25, 30]
divbt = filter(lambda x: x % 3 == 0, numbers)
square = map(lambda x: x ** 2, divbt)
adding = reduce(lambda x, y: x + y, square)
print(adding)