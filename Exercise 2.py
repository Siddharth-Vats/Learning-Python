# Exercise 2 - Faulty Calculator
# 45 *3 = 555, 56+9 =77,56/6 =4
# Design a calculator will will correctly solve all the questions except:
# 45 *3 = 555, 56+9 =77,56/6 =4
# Your program should take operator and input from the user and then return the result

var1 = int(input("Enter first number - "))
opt =  input("Enter the operator - ")
var2 = int(input("Enter second number - "))
if var1 == 45 and var2 == 3 and opt == '*':
    print(555)   
elif var1 == 56 and var2 == 9 and opt == '+':
    print(77)
elif var1 == 56 and var2 == 6 and opt == '/':
    print(4)   
else :
    if opt == '+':
        print(var1 + var2)
    elif opt == '-':
        print(var1 - var2)
    elif opt == '*':
        print(var1 * var2)
    elif opt == '/':
        print(var1 / var2)