#   １つの整数 x を読み込み、それをそのまま出力するプログラム
i = 1
while True:
    x = int(input())
    if x == 0:
        break
    print("Case {0}: {1}".format(i, x))
    i += 1