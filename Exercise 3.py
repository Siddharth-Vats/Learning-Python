

# no. of guesses = 9
# print no. of guesses left
# no. of guesses he took to finish
# print game over

n = 45
i = 0
chance = 0
while i <= 9:
    inp = int(input("Enter a number :- "))
    if inp == n:
        print("Congrats you won in ", chance + 1, "chances")
        break
    elif inp < n:
        print("Lesser!! try again and chances left is -", 8 - chance)
        chance = chance + 1
    else:
        print("Greater!! try again and chances left is -", 8 - chance)
        chance = chance + 1
    if chance == 9:
        print("GAME OVER!!")
        break
