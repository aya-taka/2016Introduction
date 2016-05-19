#   文字列 str に対して、与えられた命令の列を実行するプログラム

#   加工対象文字列strを標準入力から取得
str = list(input())
#   加工命令回数pを標準入力から取得
p = int(input())
str = "".join(str).split()
if str[0] == "print":
    print(str[0])
elif str[0] == "reverse":
    pass
elif str[0] == "replace":
    pass