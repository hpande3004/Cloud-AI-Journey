'''Level 2 Tasks Day 3
6. Count how many times each element appear in tuple'''
t = (1, 2, 3, 2, 4, 1, 5, 1)
dict = {}
for i in t:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

'''7. Find common elements between 2 lists using sets'''
list1 = [1,3,5,7]
list2 = [1,2,4,6]
set1 = set((list1))
set2 = set((list2))
set3 = set1.intersection(set2)
set3 = list(set3)
print("Common elements between 2 lists are: ", set3)

'''8. Find the elements that are in list1 but not in list2 using sets'''
l1 = [1,2,3,4]
l2 = [5,4,2,6]
diff = set(l1) - set(l2)
print(diff)

'''9. Merge 2 sets and print the result'''
s1 = {"apple", "banana", 1, "boy"}
s2 = {"car", "table", 16, "truck"}
s3 = s1.union(s2)
print(s3)