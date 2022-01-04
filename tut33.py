# l = 10 # Global variable
# def function1(n):
#     # l = 5 # Local variable
#     m = 8
#     global l
#     l = l + 5
#     print(l, m)
#     print(n, "I am printed here")
# function1("This is me")
# print(l)


x= 89
def siddharth():
    x = 20
    def parth():
        global x
        x = 88
    print("before calling parth()", x)
    parth()
    print("after calling parth()", x)

siddharth()
print(x)