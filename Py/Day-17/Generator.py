'''Generator'''
def num():
    yield 1
    yield 2
    yield 3
for i in num():
    print(i)

def numb():
    for i in range(1,6):
        yield i
for n in numb():
    print(n)

x = (j * j for j in range(1,7))
for k in x:
    print(k)