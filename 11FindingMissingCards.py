haveTrumps = [[0 for i in range(13)] for j in range(4)]
allCards = int(input())
for i in range(0, allCards):
    cardType, cardNum = input().split()
    if cardType == "S":
        haveTrumps[0][int(cardNum) - 1] = 1
    elif cardType == "H":
        haveTrumps[1][int(cardNum) - 1] = 1
    elif cardType == "C":
        haveTrumps[2][int(cardNum) - 1] = 1
    elif cardType == "D":
        haveTrumps[3][int(cardNum) - 1] = 1
for i in range(0, 4):
    for j in range(0, 13):
        if haveTrumps[i][j] == 0:
            if i == 0:
                print("S ", end="")
            elif i == 1:
                print("H ", end="")
            elif i == 2:
                print("C ", end="")
            elif i == 3:
                print("D ", end="")
            print("{0}".format(j + 1))