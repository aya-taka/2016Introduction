#   カードの山の最初の並び（文字列）と h の列をを読み込み、最後の並び（文字列）を出力するプログラム

#   カードの山の初期状態を保存する配列を定義
cardList = []
#   山札と操作を取得
while 1:
    temp = input()
    #   "-"入力で取得処理終了
    if temp == "-":
        cardList += temp
        break
    #   アルファベットならば一つのまとまりとして構成
    if temp.isalpha:
        temp = "".join(temp).split()
    #   リストに代入
    cardList += temp
#   print(cardList)
#   山札の操作
for i in range(len(cardList)):
    #   "-"が出現したら処理終了
    #   whileループ内で読み込んでいる
    if cardList[i] == "-":
        break
    #   アルファベットならば山札の情報である
    if cardList[i].isalpha():
        editCard = cardList[i]
        #   山札を実際の処理対象editcardに代入し、指定された操作回数分だけループ内でシャッフル処理を行う
        for j in range(i + 2, int(cardList[i + 1]) + i + 2):
            #   次の山札・終端指定が現れたら強制終了(ないと思うが一応)
            if cardList[j].isalpha() or cardList[j] == "-":
                break
            #   シャッフル用に山札を二重に
            editCard = editCard + editCard
            #   操作によって指定された部分を抜き出す
            editCard = editCard[int(cardList[j]):len(cardList[i]) + int(cardList[j])]
        print("{0}".format(editCard))