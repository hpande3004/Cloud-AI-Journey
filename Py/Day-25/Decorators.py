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


def my_decor(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper  
@my_decor
def greet():
    print("Hello Harshit!")
greet()

#DIY Exercise
def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper

@login_required
def login():
    print("Welcome to the dashboard!")
login()