# list1 = [["Siddharth", 34], ["Parth", 50 ], ["Shreyas", 60],["Munnu", 100]]
# # print(list1[0],list1[1],list1[2],list1[3])
# dict1 = dict(list1)
# # for item in list1:
# #     print(item)
# # for item, lollipop in list1:
# #     print(item, lollipop)
# for item, lollipop in dict1.items():
#     print(item, "and the lolly is",lollipop)

# QUICK QUIZ

list1 = ["Siddharth", 6, 7, "papaya", 110]

for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)