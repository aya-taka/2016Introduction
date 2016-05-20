#   1~nまでの間の3つの数値を足し合わせた数がx組み合わせの数を求めるプログラム
while 1:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    cnt = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if i + j + k == x and i != j and i != k and j != k:
                    cnt += 1
                    #   print("{0} {1} {2}".format(i, j, k))
    print("{0}".format(cnt))