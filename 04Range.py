#   数値a,b,cを読み込んで、a<b<cであればYes、そうでなければNoと出力するプログラム
a, b, c = map(int, input().split())
if a < b < c:
    print("Yes")
else:
    print("No")