# a = "Good Morning!"

# print(a[:5])

# for i in range(0, len(a)):
#     print(a[i])
    
# print("Good" in a)

# print("Bad" not in a)

# print(a[-5:-1])

# print(a.upper())
# print(a.lower())
# print(a.title())            #Converts to title case
# print(a.strip())            #Removes whitespaces
# print(a.replace("Morning", "Night"))
# print(a.find("Morning"))    #Returns the index of the first occurrence of the substring
# print(a.count("o"))         #Returns the number of occurrences of the substring
b = "Python is a programming language"
c = b.split()
print(len(c))

#-----------------FUNCTIONS-----------------
#Basic functions
def greet(name):
    print("Hello,", name, "!")
greet("Harshit")

def calc_sal(hours, rate):
    salary = hours * rate
    return salary
pay = calc_sal(40, 100)
print(pay)                              #RETURN usage
