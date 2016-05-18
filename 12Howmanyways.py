#   1~nまでの間の3つの数値を足し合わせた数がx組み合わせの数を求めるプログラム
while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    ansCount = 0
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                if i + j + k == x:
                    ansCount += 1
                    print("{0} {1} {2}".format(i, j, k))
    print("{0}".format(ansCount))