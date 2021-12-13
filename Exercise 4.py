# Pattern Printing
# input = integer n
# boolean = True or False

# True
# *
# **
# ***
# ****

# False
# ****
# ***
# **
# *




n = int(input("Enter a number: "))
boolean = int(input("Enter 0 or 1 : "))

if boolean == 0:
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

elif boolean == 1:
    for i in range(n):
        for j in range(n-i):
            print("* ", end="")
        print()

else:
    print("INCORRECT VALUE")    