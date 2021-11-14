mystr ="Siddharth is a good boy"
# print(len(mystr))
# print(mystr[0:9])
# print(mystr[0:99])
# print(mystr[0:]) # take the length of the string
# print(mystr[:9]) # take the begenning of the string
# print(mystr[0:9:2]) # to skip characters by index 2
# print(mystr[0:len(mystr)])



# NEGATIVE INDEXING
# print(mystr)
# print(mystr[-8:-4])
# print(mystr[::-1]) # Reverses The string

# STRING FUNCTIONS

print(mystr.isalnum()) # alpha numeric means it contains spaces
print(mystr.isalpha()) # alpha numeric means it contains spaces
print(mystr.endswith("boy")) 
print(mystr.count("dd")) # counts the given characters in a given string
print(mystr.capitalize()) # capitalizes the first letter of the given string
print(mystr.find("is")) # finds the given characters in a given string
print(mystr.lower()) # converts the characters in lower case
print(mystr.upper()) # converts the characters in upper case
print(mystr.replace("a", "the"))