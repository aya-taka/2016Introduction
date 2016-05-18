#   n×mの行列 A と m×l の行列 B を入力し、それらの積である n×l の行列 C を出力するプログラム
n, m, l = map(int, input().split())
#   n x m 行列の生成
A = [[0 for i in range(m)] for j in range(n)]
#   m x l 行列の生成
B = [[0 for i in range(l)] for j in range(m)]
#   n x l 行列(出力行列)の生成
C = [[0 for i in range(l)] for j in range(n)]

#   m x n 行列を標準入力から読み込む
for i in range(0, n):
    A[i][:m] = map(int, input().split())
    #   print(sheet_nxm)
#   m x n 行列を標準入力から読み込む
for i in range(0, m):
    B[i][:l] = map(int, input().split())
    #   print(sheet_mxl)
#   C(n x l)行列の計算　A行列とB行列の積
for i in range(0, n):
    for j in range(0, l):
        for k in range(0, m):
            C[i][j] += A[i][k] * B[k][j]
#   print(C)
#   C行列の出力
for i in range(0, n):
    for j in range(0, l):
        print("{0}".format(C[i][j]), end="")
        if j != l - 1:
            print(" ", end="")
        else:
            print("")