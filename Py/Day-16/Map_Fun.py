'''MAP()'''
numbers = [1,2,3,4,5]
sq = map(lambda x: x*x, numbers)
print(list(sq))

num = [10,20,30,40,50]
result = map(lambda x: x+5, num)
print(list(result))