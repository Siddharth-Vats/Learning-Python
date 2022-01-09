# Lambada functions or anonymous functions

# def add(a,b):
#     return a+b

# minus = lambda x, y: x-y # is equal to minus function

# def minus(a,b):
#     return a-b

# print(minus(9,4))

# def a_first(a):
#     return a[1]

# a = [[3,5], [23,67], [32, 65]]
# a.sort(key=a_first)
# print(a)

a = [[3,5], [23,67], [32, 65]]
a.sort(key= lambda x : x[1])
print(a)