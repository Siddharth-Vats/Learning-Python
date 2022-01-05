# Snake Water and Gun GAME
import random



c = 0
upt = 0
cpt = 0

while c<10:
    print("\nEnter your input")
    userInput = input("TYPE\n\t\"s\" - for snake\n\t\"w\" - for water\n\t\"g\" - for gun\n")
    lst = ['s', 'w', 'g']
    rand = random.choice(lst)
    # print(rand)

    if userInput == "S" or userInput == "s":
        c = c+1
        if rand == 's':
            print("Its a TIE!!")
            
        elif rand == 'w':
            upt+=1
            print("you WON!!")
        else:
            cpt += 1
            print("you LOST!! try again")

    elif userInput == "W" or userInput == "w":
        c = c+1
        if rand == 's':
            cpt+=1
            print("you LOST!! try again")
            # c = c+1
        elif rand == 'w':
            print("Its a TIE!!")
        else:
            upt += 1
            print("you WON!!")

    elif userInput == "G" or userInput == "g":
        c = c+1
        if rand == 's':
            upt+=1
            print("you WON!!")
            # c = c+1
        elif rand == 'w':
            cpt+=1
            print("you LOST!! try again")
        else:
            print("Its a TIE!!")

    else:
        c = c+1
        print("INCORRECT INPUT")

if cpt>upt:
    print("\nYOU LOST THE GAME!! \n\tcomputer's score is %s\n\tyour score is %s"%(cpt,upt))

elif cpt<upt:
    print("\nYOU WON THE GAME!! \n\tcomputer's score is %s\n\tyour score is %s"%(cpt,upt))

else:
    print("\nITS A BIG TIEEE!! \n\tcomputer's score is %s\n\tyour score is %s"%(cpt,upt))