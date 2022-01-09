with open("siddharth.txt") as f:
    a = f.read(9)
    print(a)

f = open("siddharth.txt", "rt")
print(f.read())
f.close()