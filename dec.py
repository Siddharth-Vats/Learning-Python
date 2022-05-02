# def function1():
#     print("Siddharth")
    
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
    
# a = funcret(1)
# print(a)

# def executor(func):
#     func("This")
    
# executor(print)

from __future__ import with_statement


def dec1(func1):
    def nowexec():
        print("Excutinng now")
        func1()
        print("now executed")
    return nowexec

@dec1
def who_is_siddharth():
    print("Siddharth is a good boy")

# who_is_siddharth = dec1(who_is_siddharth)
who_is_siddharth()