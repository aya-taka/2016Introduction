#   ３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラム
a, b, c = map(int, input().split())
#   約数の数をカウントアップする変数
divisor_count = 0
#   cを割る変数　初期値a、範囲a<DivideNum<b
divide_num = a
for i in range(a, b + 1):
    if c % divide_num == 0:
        divisor_count += 1
    divide_num += 1
print("{0}".format(divisor_count))