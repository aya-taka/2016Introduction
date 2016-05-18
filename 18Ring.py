#   リング状の文字列 s の任意の位置から、時計回りに連続した文字をいくつか選んで、文字列 p が作れるかを判定するプログラム
#   リング状の文字列sを標準入力から読み込み
s = list(input())
#   判定対象文字列pを標準入力から読み込み
p = list(input())
#   文字列sを疑似的にループさせるため、sの後にsを追加
s = s + s
#   print(s)
#   作成可能かどうか判定を行うフラグ
flag = 0
for i in range(len(s) // 2):
    if s[i] == p[0]:
        for j in range(len(p)):
            if s[i + j] != p[j]:
                break
            if j == len(p) - 1:
                flag = 1
if flag == 1:
    print("Yes")
else:
    print("No")