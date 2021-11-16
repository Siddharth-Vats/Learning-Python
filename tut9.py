"""
LISTS are mutable
"""

grocery = ["Harpic", "Mouse", "Macbook", "Computer", 77]
# print(grocery[2])

numbers = [2,3,3,654,53,5,6,2,5]
# numbers.sort()
# numbers.reverse()
# print(numbers)
# print(numbers[::-1])

# LIST FUNCTIONS

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers.append(7)
# numbers.insert(3,5)
# numbers.remove(654)
# numbers.pop() # removes last element
# print(numbers)

# numbers[3] = 6
# print(numbers)

"""
TUPLES are immumatable
    to create a tuple of a single element use this syntax
    tp = (1,) # use comma
"""

# tp = (1, 2, 3) 
# # tp[1] = 8 # will throw an error
# print(tp)

# swaping two numbers using python

a = 1
b = 4

# temp = a
# a = b
# b = temp

a, b = b, a
print(a, b)