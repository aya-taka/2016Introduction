#   ２つの n 次元ベクトルから、p がそれぞれ 1、2、3、∞∞ のミンコフスキー距離を求めるプログラム
#   次元数nを標準入力から取得
n = input()
#   ベクトルxを標準入力から取得
x = list(input())
x = "".join(x).split()
#   ベクトルyを標準入力から取得
y = list(input())
y = "".join(y).split()
#   p=1,2,無限大の時のミンコフスキー距離を格納する配列
dxy = []
for i in range(0, n):
    pass