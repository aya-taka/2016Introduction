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
    #   "print"に対する処理
    #   printの次の数値から、そのさらに次の数値までの文字列を出力
    if orderList[i][0] == "print":
        print("{0}".format(str[int(orderList[i][1]):int(orderList[i][2]) + 1]))
    #   "reverse"に対する処理
    #   reverseの次の数値から、そのさらに次の数値までの文字列を反転
    #   s = s[:a] + s[a:b+1][::-1] + s[b+1:]がきれい
    elif orderList[i][0] == "reverse":
        str = str[0:int(orderList[i][1])] + str[-len(str) + int(orderList[i][2]):-len(str) + int(orderList[i][1]) - 1:-1] + str[int(orderList[i][2]) + 1:]
    #   "replace"に対する処理
    #   指定された範囲を、指定された文字列で置き換える
    elif orderList[i][0] == "replace":
        str = str[:int(orderList[i][1])] + orderList[i][3] + str[int(orderList[i][2]) + 1:]