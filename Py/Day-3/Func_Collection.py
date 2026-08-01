'''Level 4 Tasks Day 3
13. Write a function that accepts a list and returns the average.'''
def calc_avg(num):
    if not num:
        return 0
    return sum(num) / len(num)
list = [10, 20, 40, 60, 70]
avg = calc_avg(list)
print("Avg of the list: ", avg)

#14. Write a function that returns the second largest number in a list

#15. A func that removes duplicate values from the list
    