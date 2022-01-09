num1 = input("Enter first number ")
num2 = input("Enter second number ")
try:
    print("SUM:", int(num1+num2))
except Exception as e:
    print(e) # prints the error
print("This line is very important")