#   1つの単語 W と文章 T ,T の中にある W の数を出力するプログラム
import sys
#   単語Wの取得
w = input()
#   文章Tの定義
t = []
#   文章Tの取得
for line in sys.stdin:
    t.append(line)
    if line.find("END_OF_TEXT") == -1:
        break
print(t)