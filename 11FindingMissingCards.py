have_trumps = [[0 for i in range(13)] for j in range(4)]
all_cards = int(input())
for i in range(0, all_cards):
    card_type, card_num = input().split()
    if card_type == "S":
        have_trumps[0][int(card_num) - 1] = 1
    elif card_type == "H":
        have_trumps[1][int(card_num) - 1] = 1
    elif card_type == "C":
        have_trumps[2][int(card_num) - 1] = 1
    elif card_type == "D":
        have_trumps[3][int(card_num) - 1] = 1
for i in range(0, 4):
    for j in range(0, 13):
        if have_trumps[i][j] == 0:
            if i == 0:
                print("S ", end="")
            elif i == 1:
                print("H ", end="")
            elif i == 2:
                print("C ", end="")
            elif i == 3:
                print("D ", end="")
            print("{0}".format(j + 1))