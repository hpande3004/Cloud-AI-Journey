def reverse_str(string):
    for i in string:
        return string[::-1]


def count_vowles(str):
    vowel_c = 0
    for f in str.lower():
        if f in "aeiou":
            vowel_c += 1
    return vowel_c