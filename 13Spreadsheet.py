#   表の行数rと列数c、r × c の要素を持つ表を読み込んで、各行と列の合計を挿入した新しい表を出力するプログラム
r, c = map(int, input().split())
spreadSheet = [[0 for i in range(c + 1)] for j in range(r + 1)]
#   表入力の受付
for i in range(0, r):
    spreadSheet[i][:c] = map(int, input().split())
    #   print(spreadSheet)
#   行方向合計の算出
for i in range(0, r):
    for j in range(0, c):
        spreadSheet[i][c] += spreadSheet[i][j]
#   列方向合計の算出
for i in range(0, c + 1):
    for j in range(0, r):
        spreadSheet[r][i] += spreadSheet[j][i]
#   print(spreadSheet)
for i in range(0, r + 1):
    for j in range(0, c + 1):
        print("{0}".format(spreadSheet[i][j]), end="")
        if j != c:
            print(" ",end="")
        else:
            print("")