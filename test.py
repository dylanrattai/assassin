playerList = ["name1", "name2", "name3", "name4", "name5", "name6", "name7"]
charOpinions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
playerCount = 6

def opinionDown(input):
    if input in playerList:
            if input == playerList[0]:
                charOpinions[0] = charOpinions[0] - 1
                return True
            elif input == playerList[1]:
                charOpinions[1] = charOpinions[1] - 1 
                return True
            elif input == playerList[2]:
                charOpinions[2] = charOpinions[2] - 1 
                return True
            elif input == playerList[3]:
                charOpinions[3] = charOpinions[3] - 1 
                return True
            elif input == playerList[4]:
                charOpinions[4] = charOpinions[4] - 1 
                return True
            elif input == playerList[5]:
                charOpinions[5] = charOpinions[5] - 1 
                return True
            elif input == playerList[6]:
                charOpinions[6] = charOpinions[6] - 1 
                return True
            elif input == playerList[7]:
                charOpinions[7] = charOpinions[7] - 1 
                return True
            elif input == playerList[8]:
                charOpinions[8] = charOpinions[8] - 1 
                return True
            elif input == playerList[9]:
                charOpinions[9] = charOpinions[9] - 1 
                return True
            elif input == playerList[10]:
                charOpinions[10] = charOpinions[10] - 1 
                return True
            elif input == playerList[11]:
                charOpinions[11] = charOpinions[11] - 1 
                return True
    else:
        print("ERROR in opinionDown")

def  test(upDn, char):
    global charOpinions

    for x in range(playerCount):
        if playerList[x] == char:
            if upDn == "down":
                charOpinions[x] = charOpinions[x] - 1
            elif upDn == "up":
                charOpinions[x] = charOpinions[x] + 1
            else:
                print("ERROR in test")

print(test("down", "name5"))
print(charOpinions[4])