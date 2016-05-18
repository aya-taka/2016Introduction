#   n×mの行列 A と m×l の行列 B を入力し、それらの積である n×l の行列 C を出力するプログラム
n, m, l = map(int, input().split())
#   n x m 行列の生成
sheet_nxm = [[0 for i in range(m)] for j in range(n)]
#   m x l 行列の生成
sheet_mxl = [[0 for i in range(l)] for j in range(m)]
#   m x n 行列を標準入力から読み込む
for i in range(0, n):
    sheet_nxm[i][:m] = map(int, input().split())
    #   print(sheet_nxm)
#   m x n 行列を標準入力から読み込む
for i in range(0, m):
    sheet_mxl[i][:l] = map(int, input().split())
    #   print(sheet_mxl)