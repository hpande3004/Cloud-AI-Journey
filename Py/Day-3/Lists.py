'''LEVEL 1 Tasks Day 3
1. Largest num in a list'''
num = [3, 5, 7, 6, 8, 2]
large_num = num[0]
for i in num:
    if i > large_num:
        large_num = i
print("Largest number in the list is:", large_num)

'''2. Smallest num in a list'''
small_num = num[0]
for i in num:
    if i < small_num:
        small_num = i
print("Smallest num in the list: ", small_num)

'''3. Count how many even and odd numbers in a list'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for i in list1:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers in the list: ", even)
print("Odd numbers in the list: ", odd)

'''4. Reverse list without using reverse() method'''
n = [6, 8, 10, 12, 14]
rev_n = []
for i in range(len(n)-1, -1, -1):
    rev_n.append(n[i])
print("Reversed list: ", rev_n)

'''5. Remove duplicates from a list'''
list2 = [1,2,2,3,3,4,4,4,5,6,8,9,9]
uniq = []
for i in list2:
    if i not in uniq:
        uniq.append(i)
print(uniq)