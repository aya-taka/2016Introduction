#   ３つの整数 a、b、c を読み込み、a から b までの整数の中に、c の約数がいくつあるかを求めるプログラム
a, b, c = map(int, input().split())
#   約数の数をカウントアップする変数
cnt = 0
for i in range(a, b + 1):
    if c % i == 0:
        cnt += 1
print("{0}".format(cnt))