#   ２つの n 次元ベクトルから、p がそれぞれ 1、2、3、∞∞ のミンコフスキー距離を求めるプログラム
import math
#   次元数nを標準入力から取得
n = int(input())
#   ベクトルxを標準入力から取得
x = list(input())
x = "".join(x).split()
#   ベクトルyを標準入力から取得
y = list(input())
y = "".join(y).split()
#   p=1,2,無限大の時のミンコフスキー距離を格納する配列
#   合わせて初期化
dxy = [0 for i in range(4)]
#   p=1の時のミンコフスキー距離の計算
for i in range(0, n):
    dxy[0] += math.fabs(int(x[i]) - int(y[i]))
#   p=2
for i in range(0, n):
    dxy[1] += (math.fabs(int(x[i]) - int(y[i]))) ** 2
dxy[1] = math.sqrt(dxy[1])
#   p=3
for i in range(0, n):
    dxy[2] += (math.fabs(int(x[i]) - int(y[i]))) ** 3
dxy[2] = math.pow(dxy[2], 1.0 / 3.0)

print(dxy[2])