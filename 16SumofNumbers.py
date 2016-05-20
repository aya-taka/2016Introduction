#   与えられた数の各桁の和を計算するプログラム
while 1:
    #   標準入力から数値読み込み
    input_num = list(input())
    #   終了判定　"0"入力で終了
    if int(input_num[0]) == 0:
        break
    #   print(input_num)
    #   各桁合計を保存する変数
    digit_total = 0
    for i in range(0, len(input_num)):
        digit_total += int(input_num[i])
    print("{0}".format(digit_total))