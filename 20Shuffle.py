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
print(cardList)
for i in range(len(cardList)):
    if cardList[i].isalpha():
        pass