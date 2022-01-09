# f = open("siddharth.txt", "w") # to write something
# f = open("siddharth.txt", "a") # to append something
# a = f.write("Siddharth bahut aacha hain")
# print(a)
# f.close()

# Read and Write both

f = open("siddharth.txt", "r+")
print(f.read())
f.write("\n\tthank you")
f.close()