# # Health Management System
# # 3 clients - Siddharth, Parth and Shreyas


def getdate():
    import datetime
    return datetime.datetime.now()


# # Total 6 files
# # Write a function that when executed takes as input client name
# cable crossover
# one more function to retrive exercise or food for any client

dati = "[" + str(getdate()) + "] "


# tf = True
# tft = False
# inp = int(input("Do you want to run the program again\n\tTYPE\n\t0for yes\n\t1 for no"))
# if inp == 0:
#     tft = True
#
# tf = tft


def addLog():
    print("Enter the client name:")
    clientName = int(input("\t1 for Siddharth\n\t2 for Parth\n\t3 for Shreyas"))
    if clientName == 1:

        workDiet = int(input("TYPE:\n\t1 for diet\n\t2 for work out"))

        if workDiet == 1:
            f = open("siddharthdiet.txt", "a")
            print("What you ate now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)

        else:
            f = open("siddharthworkout.txt", "a")
            print("What work out you did now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)
        f.close()

    if clientName == 2:
        workDiet = int(input("TYPE:\n\t1 for diet\n\t2 for work out"))

        if workDiet == 1:
            f = open("parthdiet.txt", "a")
            print("What you ate now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)

        else:
            f = open("parthworkout.txt", "a")
            print("What work out you did now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)
        f.close()

    if clientName == 3:
        workDiet = int(input("TYPE:\n\t1 for diet\n\t2 for work out"))

        if workDiet == 1:
            f = open("shreyasdiet.txt", "a")
            print("What you ate now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)

        else:
            f = open("shreyasworkout.txt", "a")
            print("What work out you did now")
            add = input("Type here\n\t")

            f.write(dati)
            add += "\n"
            f.write(add)
        f.close()


def retrieveLog():
    print("Whose data you want to retrieve")
    inp = int(input("TYPE\n\t1 for Siddharth\n\t2 for Parth\n\t3 for Shreyas"))
    inpDiet = int(input("TYPE\n\t1 for diet\n\t2 for workout"))
    if inp == 1:
        if inpDiet == 1:
            with open("siddharthdiet.txt") as f:
                for line in f:
                    print(line)
        elif inpDiet == 2:
            with open("siddharthworkout.txt") as f:
                for line in f:
                    print(line)

    if inp == 2:
        if inpDiet == 1:
            with open("parthdiet.txt") as f:
                for line in f:
                    print(line)
        elif inpDiet == 2:
            with open("parthworkout.txt") as f:
                for line in f:
                    print(line)

    if inp == 3:
        if inpDiet == 1:
            with open("shreyasdiet.txt") as f:
                for line in f:
                    print(line)
        elif inpDiet == 2:
            with open("shreyasworkout.txt") as f:
                for line in f:
                    print(line)


def check():
    print("Do you want to add or retrieve")
    inp = int(input("TYPE\n\t1 to add\n\t2 to retrieve"))

    if inp == 1:
        addLog()
    elif inp == 2:
        retrieveLog()
    else:
        print("invalid input")


run = True
inp = input("Do you want to run the program\nTYPE\n\t1 for yes\n\t0 for no\n")

while inp == "1":
    if inp == "1":
        check()
        inp = input("Do you want to run the program again\nTYPE\n\t1 for yes\n\t0 for no\n")
    else:
        break
