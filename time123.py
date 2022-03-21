import time

initial = time.time()
# print(initial)

j = 0
while j<45:
    print("This is Siddharth")
    time.sleep(2) 
    j+= 1

print("While loop ran in ",time.time() - initial ,"seconds")

for i in range(45):
    print("This is Siddharth")

initial2 = time.time()
print("for loop ran in ", time.time() - initial2 ,"seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(type(localtime))
# print(localtime)