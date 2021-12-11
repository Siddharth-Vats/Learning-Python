f = open("siddharth.txt", "r")
# print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())


# content = f.read()
# print(content)

for line in f:
    print(line)

# content = f.read(3344)
# print(content)
# content = f.read(344)
# print(content) # will not return same value
f.close() # always close the opened file