# F STRING
import math
import time

me = "Siddharth"
a1 = 3
# a = "This is %s"%me
# a = "This is %s %s"%(me, a1)

# a = "This is {} {}"
# a = "This is {1} {0}" # Swapa me and a1
# b = a.format(me, a1)
a = f"This is {me} {a1} {4*60} {math.cos(65)}"  # this is real fstring

print(a)
# print(b)