'''Decorators'''


def my_dec(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

def greet():
    print("Hello Harshit!")
greet = my_dec(greet)
greet()