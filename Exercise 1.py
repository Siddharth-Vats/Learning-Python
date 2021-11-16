# Create a dictionary and take input from the user and return the meaning of the word from the dictionary.
myDict = {"Hello" : "Used to greet someone",
          "Abandon" : "to leave",
          "pardon" : "to forgive",
          "university" : "collection of colleges"}
print(myDict.keys())
inp = input("Enter the word from the given list :")
print(myDict.get(inp))
