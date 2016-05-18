#   1つの単語 W と文章 T ,T の中にある W の数を出力するプログラム
import sys
#   単語Wの取得
w = input()
#   文章Tの定義
t = []
#   文章Tの取得
while 1:
    temp = input()
    if temp == "END_OF_TEXT":
        break
    t += temp.strip(".")
    t += " "
#   文字列を結合
t = "".join(t).split()
#   print(t)
#   文章T内に存在する単語Wのカウントを行う
count = 0
for i in range(len(t)):
    if t[i].lower() == w:
        count += 1
print(count)
