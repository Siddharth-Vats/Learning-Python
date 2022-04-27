# ---------------------MAP-------------------

# numbers = ["3", "34", "47"]
# numbers = list(map(int, numbers))
# # for item in range(len(numbers)):
# #     numbers[item] = int(numbers[item])
    
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a

# num = [3,43,4,54,45,64,45,45,4,4]
# square = list(map(sq,num))
# print(square)

# num = [3,43,4,54,45,64,45,45,4,4]
# square = list(map(lambda x: x*x,num))
# print(square)


# square = lambda a: a*a
# cube = lambda a: a*a*a
# func = [square, cube]

# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# --------------------------FILTER---------------------------------

# list1 = [1,2,3,4,5,6,7,8,9]

# is_greater_5 = lambda num: num>5

# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)

# ------------------------REDUCE-----------------------

from functools import reduce

list1 = [1,2,3,4]

num = reduce(lambda x,y:x*y, list1)

# num = 0
# for i in list1:
#     num = num + i
    
print(num)

