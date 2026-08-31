'''Practice Codes'''
#1: iter() + next()
numbers = [10, 20, 30, 40, 50]
num = iter(numbers)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

print("-----------------")

#2: Generator
def count_num():
    for i in range(1,6):
        yield i
for k in count_num():
    print(k)

print("-----------------")

#3: Even numbers generator + loop
def even():
    for i in range(1,21):
        if i % 2 == 0:
            yield i
for j in even():
    print(j)

print("-----------------")

#4: Generator challenge
def sqr(n):
    for x in range(1, n+1):
        yield x * x
for num in sqr(5):
    print(num)