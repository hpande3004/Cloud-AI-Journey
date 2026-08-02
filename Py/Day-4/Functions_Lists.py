'''Task 1 Day 4
Q1. Write a function that returns the largest number in a list.'''
# def largest(num):
#     large = max(num)
#     print(large)
# list = [90, 91, 84, 65, 99, 105, 101]
# largest(list)

#Q2. Smallest number in the list
# def smallest(num):
#     small = min(num)
#     print(small)
# list = [90, 91, 84, 65, 99, 105, 101]
# smallest(list)

#Q3. Even numbers in list
# def even(numbers):
#     count = 0
#     for x in numbers:
#         if x % 2 == 0:
#             count += 1
#     return count
# list = [12, 18, 25, 26, 33, 38, 44, 47, 55, 56, 58, 60, 66]
# result = even(list)
# print(result)

#Q4. Avg of nums
def avg(num):
    t = 0
    for x in num:
        t += x
    return t / len(num)
list = [1,3,5,7,8,6,4,2]
print(avg(list))