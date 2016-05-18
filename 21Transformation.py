#   文字列 str に対して、与えられた命令の列を実行するプログラム

while 1:
    str = list(input())
    str = "".join(str).split()
    if str[0] == "print":
        print(str[0])
    elif str[0] == "reverse":
        pass
    elif str[0] == "replace":
        pass