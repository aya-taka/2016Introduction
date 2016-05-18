#   与えられた英文に含まれる、各アルファベットの数を数えるプログラム
#   標準入力から文字列読み込み

import sys
#   改行を含む文字列を読み込み
input_char = []
for line in sys.stdin:
    input_char.append(line)
#   文字列をすべて結合
count_char = "".join(input_char)
#   print(count_char[2])
#   文字カウント用配列の定義
countingChar = [0 for i in range(26)]
#   カウントアップ処理
for i in range(0, len(count_char)):
    if ord(count_char[i].lower()) - ord("a") > -1 and ord(count_char[i].lower()) - ord("a") < 27:
        countingChar[ord(count_char[i].lower()) - ord("a")] += 1
#   出力
for i in range(0, 26):
    print("{0} : {1}".format(chr(ord("a") + i), countingChar[i]))