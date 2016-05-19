#   文字列 str に対して、与えられた命令の列を実行するプログラム

#   加工対象文字列strを標準入力から取得
str = list(input())
str = "".join(str)
#   加工命令回数pを標準入力から取得
p = int(input())
#   p個の命令を保持する配列の定義
orderList = [0 for i in range(p)]
for i in range(0, p):
    orderList[i] = list(input())
    orderList[i] = "".join(orderList[i]).split()
    if orderList[i][0] == "print":
        print("{0}".format(str[int(orderList[i][1]) - 1:int(orderList[i][2])]))
    elif orderList[i][0] == "reverse":
        str = str[0:int(orderList[i][1]) - 1] + str[-len(str) + int(orderList[i][2]) - 1:-len(str) + int(orderList[i][1]) - 2:-1] + str[int(orderList[i][2]):len(str)]
    elif orderList[i][0] == "replace":
        pass