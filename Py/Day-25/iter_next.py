'''Iterator and Next'''
num = [10, 20, 30, 40, 50]
it = iter(num)  # Create an iterator from the list
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

fruit = ['apple', 'banana', 'cherry']
ite = iter(fruit)
print(next(ite))
print(next(ite))
print(next(ite))

#With try and except
fruit = ['apple', 'banana', 'cherry']
iterator = iter(fruit)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))  # This will raise StopIteration
except StopIteration:
    print("Reached the end of the iterator.")