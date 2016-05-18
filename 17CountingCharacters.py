#   与えられた英文に含まれる、各アルファベットの数を数えるプログラム
#   標準入力から文字列読み込み
input_char = list(input())
countingChar = [0 for i in range(26)]
for i in range(0, len(input_char)):
    if ord(input_char[i].lower()) - ord("a") > -1 and ord(input_char[i].lower()) - ord("a") < 27:
        countingChar[ord(input_char[i].lower()) - ord("a")] += 1
for i in range(0, 26):
    print("{0} : {1}".format(chr(ord("a") + i), countingChar[i]))