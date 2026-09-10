#*args and **kwargs
def calc_avg(*num):
    total = 0
    for n in num:
        total = total + n
    return total / len(num)
print(calc_avg(10,25,40,55,70,85,100))
print(calc_avg(10,20,30))                   #*args

def show_details(**kwargs):
    print(kwargs)
show_details(name="Harshit", age=22, city="Pune")

#-------------------------

def show_det(**kwargs):
    for key,value in kwargs.items():
        print(key,":", value)
show_det(name="Harshit", age=22, city="Pune")

#-------------------------

def create_profile(**details):
    for key,value in details.items():
        print(key,":",value)
create_profile(name="Harshit", role="AI Cloud Engineer", skills="Python, AWS, Azure")

#-------------------------
#args and kwargs combined
def show_detail(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
show_detail(10,20,30, name="Harshit", age=22, city="Pune")