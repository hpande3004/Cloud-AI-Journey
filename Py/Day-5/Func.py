def greet(name):
    print(name)
greet("Hello!")

def sqr(num):
    square = num ** 2
    print("Square of number is: ", square)
sqr(11)

def is_even(numb):

    if numb % 2 == 0:
        return True
    else:
        return False
result = is_even(77)
print(result)