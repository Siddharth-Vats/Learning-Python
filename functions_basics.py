# a = 9
# b = 17
# c = sum((a,b)) # built-in function




# IF NONE IS PRINTED MEANS THAT FUNCTION HAS NOT ANY RETURN TYPE

def function1(a,b):
    print("I am function 1",a+b)

def average(a,b):
    """This is a function which will calculate average""" # first commented line with tripple quotes is called docstring
    """'This function does not work for three numbers""" # it is not a docstring
    print((a+b)/2)
    return (a+b)//2
# function1(5,7)
# v = average(6,90)
# print(v)
print(average.__doc__) # to print docstring