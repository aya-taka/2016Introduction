#   ３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラム
a, b, c = map(int, input().split())
#   約数の数をカウントアップする変数
DivisorCount = 0
#   cを割る変数　初期値a、範囲a<DivideNum<b
DivideNum = a
for i in range(a, b + 1):
    if c % DivideNum == 0:
        DivisorCount += 1
    DivideNum += 1
print("{0}".format(DivisorCount))