'''Python Comprehension'''

squares = []
for i in range(1,6):
    squares.append(i*i)
print(squares)                                          #Normal method

squares = [i * i for i in range(1,6)]
print(squares)                                          #Shorter method

numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)                                          #Normal loop

numbers = [i for i in range(1,6)]
print(numbers)                                          #Shorter method

'''For even number now'''
numbers = [i for i in range(1,11) if i%2 == 0]
print(numbers)

squares = [i*i for i in range(1,11) if i%2 == 0]        #Squares of only even nums in range
print(squares)

'''String Operations'''
names = ["Rahul", "Priya", "Amit", "Sneha", "Raj"]
upper_names = [i.upper() for i in names]
print(upper_names)

long_names = [j for j in names if len(j) >= 5]
print(long_names)

'''Dictionary Comprehension'''
num = {i:i*i for i in range(1,6)}
print(num)

'''Nested Comprehension'''
matrix = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10]
]
result = []
for i in matrix:
    for num in i:
        result.append(num)
print(result)