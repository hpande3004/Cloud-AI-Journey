'''DAY-6 Cloud-AI Journey

Functions Warm up and brushing up'''

def square():
    number = int(input("Enter the number: "))
    sqr = number ** 2
    print("Square of number is: ", sqr)
square()

def cube():
    number = int(input("Enter number: "))
    cb = number ** 3
    print("Cube of number is: ", cb)
cube()

def is_even(num):
        if num % 2 == 0:
            print("Number is even.")
        else:
            print("Number is odd.")
is_even(55)

#String methods

#Reverse a str
str = "Cloud Computing"
print(str[::-1])

#Count vowel
def count_vowel(string):
    vowel_c = 0
    for x in string:
        if x.lower() in "aeiou":
          vowel_c = vowel_c + 1
    return vowel_c
result = count_vowel("printer")
print(result)

#Check if word is palindrome
def palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False
result = palindrome("naman")
print(result)

#Count whitespaces in a sentence
def whitespaces(sentence):
    whites_count = 0
    for x in sentence:
        if x == " ":
            whites_count = whites_count + 1
    return whites_count
result = whitespaces(" Py is a fun lang to learn ")
print(result)