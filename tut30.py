f = open("siddharth.txt")

print(f.tell())
print(f.readline())
print(f.seek(0)) # tell the pointer from where to read

print(f.tell())
print(f.readline())

f.close()