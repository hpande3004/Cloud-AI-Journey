#Sum of numbers in list
def myfunc(numbers):
    add = sum(numbers)
    print(add)
list = [13, 40, 55, 10, 15]
myfunc(list)

#Average of numbers in list
def average(numb):
    avg = 0
    for x in numb:
        avg = avg + x
    return avg / len(numb)
avg_nums = [34, 45, 56, 67, 78]
result = average(avg_nums)
print(result)

#Largest number to exist in a list
def element(n):
    number = max(n)
    return number
aaa = [54, 69, 72, 108, 105]
aa = element(aaa)
print(aa)

#Count number of even digits in a list
def even_number(dig):
    count = 0
    for x in dig:
        if x % 2 == 0:
            count = count + 1
    return count
list = [12, 35, 62, 31, 10, 11, 13, 32]
result = even_number(list)
print(result)