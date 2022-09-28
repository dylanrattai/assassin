import time
import random

playerCount = None
alivePlayerCount = None
alivePlayers = None
role = None
roleOptions = ["assassin", "detective", "innocent"]
playerList = []
nameOptions = ["Jacob", "Michael", "Josh", "Matt", "Ethan", "Andrew", "Daniel", "Anthony", "Chris", "Joseph", "Emily", "Emma", "Madison", "Abigail", "Olivia", "Isabella", "Hannah", "Samantha", "Ava", "Ashley"]
nc = 20 - 1
charOpinions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #scale 0-2 | 0 > = negative (targets player), 1 = neutral, 2 < = positive (will not target player)
charRoles = []

def gameStart():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAssassin")
    choice = input("1. Play\n2. Help/Info\n\n").lower()

    if choice == "2" or choice == "help" or choice == "info" or choice == "information":
        help()
    elif choice == "1" or choice == "play":
        numPlayerSelect()
    else:
        print("\n\n" + choice + " is not a valid option")
        time.sleep(3)
        gameStart()

def numPlayerSelect():
    print("\n\nSelect number of players\n(This is a one player experience)")
    choice = input("1. 6 players\n2. 8 players\n3. 10 players\n4. 12 players\n\n").lower()

    global playerCount
    global alivePlayerCount

    if choice == "1" or choice == "6 players":
        playerCount = 6
        alivePlayerCount = 6
        nameSelector()
        game()
    elif choice == "2" or choice == "8 players":
        playerCount = 8
        alivePlayerCount = 8
        nameSelector()
        game()
    elif choice == "3" or choice == "10 players":
        playerCount = 10
        alivePlayerCount = 10
        nameSelector()
        game()
    elif choice == "4" or choice == "12 players":
        playerCount = 12
        alivePlayerCount = 12
        nameSelector()
        game()
    else:
        print("\n\n" + choice + " is not a valid option")
        time.sleep(3)
        numPlayerSelect()

def help():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHelp Page\n("Return" to go back to the previous menu)')
    choice = input("1. How to play\n\n").lower()

    if choice == "1" or choice == "how to play":
        howToPlay()
    elif choice == "return":
        gameStart()
    else:
        print("\n\n" + choice + " is not a valid option")
        time.sleep(3)
        gameStart()

def howToPlay():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHow to play Assassin\n")
    #add tutorial here
    choice = input('"Return" to go back to the previous menu\n\n').lower()

    if choice == "return":
        help()
    else:
        print("\n\n" + choice + " is not a valid option")
        time.sleep(3)
        howToPlay()

def nameSelector():
    global playerList

    if playerCount == 6:
        playerList = [nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)]]
        if role == "innocent":
            det = random.randint(0, playerCount - 1)
            assassin = random.randint(0, playerCount - 1)
            charRoles[det] = ""
    elif playerCount == 8:
        playerList = [nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)]]
    elif playerCount == 10:
        playerList = [nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)]]
    elif playerCount == 12:
        playerList = [nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)], nameOptions[random.randint(0, nc)]]

#not done yet \/
def game():
    global role

    #roleNum = random.randint(0,2)
    #role = roleOptions[roleNum]
    role = "innocent"
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Players")

    for i in playerList:
        print(i)


    print("\n\n")
    print("You are " + role + "\nTurn options")

    if role == "innocent":
        innoOptions()

def innoOptions():
    choice = input("1. Accuse\n2. Do nothing\n\n").lower()

    if choice == "1" or choice == "accuse":
        accuseWho = input("Who do you want to accuse")

        if input in playerList:
            if input == playerList[0]:
                charOpinions[0] = charOpinions[0] - 1
            elif input == playerList[1]:
                charOpinions[1] = charOpinions[1] - 1 
            elif input == playerList[2]:
                charOpinions[2] = charOpinions[2] - 1 
            elif input == playerList[3]:
                charOpinions[3] = charOpinions[3] - 1 
            elif input == playerList[4]:
                charOpinions[4] = charOpinions[4] - 1 
            elif input == playerList[5]:
                charOpinions[5] = charOpinions[5] - 1 
            elif input == playerList[6]:
                charOpinions[6] = charOpinions[6] - 1 
            elif input == playerList[7]:
                charOpinions[7] = charOpinions[7] - 1 
            elif input == playerList[8]:
                charOpinions[8] = charOpinions[8] - 1 
            elif input == playerList[9]:
                charOpinions[9] = charOpinions[9] - 1 
            elif input == playerList[10]:
                charOpinions[10] = charOpinions[10] - 1 
            elif input == playerList[11]:
                charOpinions[11] = charOpinions[11] - 1 
        else:
            print("\n\n" + choice + " is not a valid option")
            time.sleep(3)
            innoOptions()

    elif choice == "2" or choice == "nothing" or choice == "do nothing":
        game2()

gameStart()