#FUNCTIONS PRACTICE
def myfun():
    print("Hello there!")
myfun()

def greet(name):
    print("Hello", name)
greet("Harshit")

def add(a, b):
    sum = a + b
    print("Sum = ",sum)
add(35, 54)

def square(a):
    sq = a ** 3
    return sq
print("Cube of num is: ", square(5))

def largest(x, y):
    if x > y:
        return x
    else:
        return y
print("The largest number among two is: ", largest(104, 250))

def display(num):
    print(num)
my_list = [29, 54, 96, 64]
display(my_list[0])

#Find the sum
def laaa(numbers):
    s = 0
    for num in numbers:
        s = s + num
    return s
marks = [90, 98, 89]
print(laaa(marks))

#Avg of numbers
def average(number):
    t = 0
    for x in number:
        t = t + x
    return t / len(number)
list = [1,3,5,7,8,6,4,2]
print(average(list))

def prpr(name):
    print("HaHaHaHa", name)
prpr("HeHeHeHe")

# #Count Vowels
def vowels(text):
    count = 0
    for x in text:
        if x.lower() in "aeiou":
            count = count + 1
    return count 
print("The number of vowels in the string are:", vowels("Cloud Computing"))

#1. Largest no in list
def even(num):
    largest = max(num)
    print("The largest number in list: ", largest)
list = [24, 13, 65, 45, 98]
even(list) 

#2. Even numbers in list
def eev(num):
    count = 0
    for i in num:
        if i % 2 == 0:
            count += 1
    print(count)
list = [24, 45, 56, 68, 77]
eev(list) 

#Reverse string
def rev(str):
    return str[::-1]                #Slicing for reverse string
result = rev("Cloud Computing")
print(result)

#Count words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)
my_sentence = "Python is an easy language to learn"
result = count_words(my_sentence)
print(result)      