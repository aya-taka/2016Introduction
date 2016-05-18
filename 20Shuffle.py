#   カードの山の最初の並び（文字列）と h の列をを読み込み、最後の並び（文字列）を出力するプログラム

#   カードの山の初期状態を保存する配列を定義
cardList = []
while 1:
    temp = input()
    if temp == "-":
        cardList += temp
        break
    if temp.isalpha:
        temp = "".join(temp).split()
    cardList += temp
#   print(cardList)
for i in range(len(cardList)):
    if cardList[i] == "-":
        break
    if cardList[i].isalpha():
        editCard = cardList[i]
        for j in range(i + 2, int(cardList[i + 1]) + i + 2):
            if cardList[j].isalpha() or cardList[j] == "-":
                break
            editCard = editCard + editCard
            editCard = editCard[int(cardList[j]):len(cardList[i]) + int(cardList[j])]
        print("{0}".format(editCard))