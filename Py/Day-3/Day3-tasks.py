# list = ["AA", "BB", "CC", "DD"]
# print(list)
# print(type(list))
# print(list[2])
# print(len(list))

#----List operations----
# list.append("EE")
# print(list)
# list.insert(1, "FF")
# print(list)
# list.remove("CC")
# print(list)
# list.pop(1)                     #only removes item of specified index
# # print(list)                     #that's the difference between remove and pop
# del list[0]                       #also removes item of specified index
# print(list)
# cars = ["BMW", "AUDI", "MERCEDES", "TOYOTA"]
# del cars                            #can also delete the entire list
# cars.clear()                          #can also clear/ empties the entire list   

# list1 = ['A','B','C','D']
# list2 = ['E','F','G','H']
# list1.extend(list2)
# print(list1)

#----Loops in list----
# list = ["AA", "BB", "CC", "DD"]
# for x in list:
#     print(x)                                #For loop

# i = 0
# while i < len(list):
#     print(list[i])                          #While loop
#     i += 1

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits.sort(reverse=True)                       #sorts the list in descending order
# print(fruits)

#Copy a list
# newlist = fruits.copy()                          #copy method
# print(newlist)
#OR
# newlist = list(fruits)                          #list method
# print(newlist)
# #OR
# newlist = fruits[:]                             #slicing method
# print(newlist)

#Join 2 lists

# list1 = ["A", "B", "C"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)                                    #Method 1
# list1.append(list2)                               
# print(list1)                                    #Method 2
# list1.extend(list2)
# print(list1)                                    #Method 3

#-------TUPLES--------
# tup = ('A', 'B', 'C', 'D')                      
# (E, F, G, H) = tup                              #Packing a tuple into variables
# print(E)   
# print(F)
# print(G)
# print(H)

#--------DICT---------
capitals = { "USA" : "Washington D.C",
             "India" : "New Delhi",
              "China" : "Beijing",
              "Russia" : "Moscow"}
# print(capitals)
# print(capitals.get("USA"))

# if capitals.get("USA"):
#     print("Capital exist!")
# else:
#     print("Capital doesn't exists!")

# capitals.update({"UK":"London"})          #adds new key value pair to the dictionary
# print(capitals)

# capitals.pop("China")                 #removes specified key value pair
# print(capitals)

# capitals.popitem()                      #removes latest key value pair
# print(capitals)

# capitals.clear()                          #clears the entire dictionary

keys = capitals.keys()
# print(keys)                           #Just to print the keys of the dictionary

# for keys in capitals.keys():
#     print(keys)                        #To print the keys of the dictionary using for loop

values = capitals.values()
# print(values)
# for values in capitals.values():
#     print(values)                      #To print the values of the dictionary using for loop

items = capitals.items()
# print(items)                           #To print the key value pairs of the dictionary using for loop

# for x, y in capitals.items():
#     print(x, ":", y)                        #To print the key value pairs of the dictionary using for loop

#--------SETS--------
set = {'A', 'B', 'C', 'D'}
set1 = {"red", "blue", "green"}
set2 = {"apple", "red", "banana"}
# print(set)
set.add('E')                          #adds new item to the set
set.remove('A')                       #removes specified item from the set

# set1.update(set2)                     #adds items from set2 to set1
# print(set1)
# set1.discard("blue")                       #removes specified item from the set
# print(set1)
x = set.pop()                              #removes random item from the set

set.clear()                               #clears the entire set

# set3 = set1.union(set2)                  #joins 2 sets
# print(set3)
# set3 = set1 | set2                          #joins 2 sets
# print(set3)

# set3 = set1.intersection(set2)
# print(set3)                               #prints common items from both sets
# set3 = set1 & set2
# print(set3)                               #prints common items from both sets
# set3 = set1.difference(set2)
# print(set3)                               #prints items from set1 that are not in set2
# set3 = set1-set2
# print(set3)                               #prints items from set1 that are not in set2
# set3 = set1.symmetric_difference(set2)
# print(set3)                               #prints items from set1 that are not in set2 and vice versa
# set3 = set1 ^ set2
# print(set3)                               #prints items from set1 that are not in set2 and vice versa

#Frozenset
# fset = frozenset({"apple", "banana", "cherry"})
# print(fset)                               #creates a frozenset which is immutable