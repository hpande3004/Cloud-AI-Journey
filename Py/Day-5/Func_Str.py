#Count vowels im a string
def count_vowels(str):
    count = 0
    for x in str:
        if x.lower() in "aeiou":
            count = count + 1
    return count
result = count_vowels("Cloud computing")
print(result)

#Reverse a string
def reverse_string(word):
    return word[::-1]
result = reverse_string("Harshit Pande")
print("Reverse of the str: ", result)

#Count upper case letters
def count_upper(word):
    count = 0
    for x in word:
        if x.isupper():
            count = count + 1
    return count
result = count_upper("AbHdYbHBudHBUCHWIbdbubsa")
print(result)

#Count words in a sentence
def count_words(sentence):
    count = 0
    for x in sentence.split():
        count += 1
    return count
sentences = "Python programming is fun to learn!"
result = count_words(sentences)
print(result)