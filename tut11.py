s = set()
# print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = (l)
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(1) # set does not keep similar values. It only retains unique values
s.remove(1)
s1 = s.union({1, 2}) 
s1 = s.intersection({1, 2})
print(s, s1)
print(len(s))