
# # n*n-1 * n-2 * ...... 1
# # n = n * (n-1)

# def factorial_iterative(n):
#     """
#         n = Integer
#         return : n*n-1 * n-2 * ...... 1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac

# def factorial_recursive(n):
#     """
#         n = Integer
#         return : n*n-1 * n-2 * ...... 1
#     """
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)


# number = int(input("Enter a number: "))
# print("factorial using iterative method is",factorial_iterative(number))
# print("factorial using recursive method is",factorial_recursive(number))



# QUICK QUIZ - Phibonachi numbers(sum of last two digits)
# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

number  = int(input("Enter a number: "))
for i in range(number):
    print(fibonacci(i), end=" ")
