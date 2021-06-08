'''def run():
    list=[1,2,3,4,5]
    li=[i**2 for i  in list ]
     #if i % 2 !=0
    print(li)
run()
my_list =[1,2,3,4,5]
squares = list(filter(lambda x: x**2,my_list))
print(squares)

my_list =[1,2,3,4,5]


squares = list(map(lambda x: x**2,my_list))
print(squares)
'''
from functools import reduce
my_list =[1,2,3,4,5]
alL= reduce(lambda a,b : a * b, my_list)
print(alL)