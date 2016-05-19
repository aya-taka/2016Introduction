#   次の展開図から得られるサイコロを転がすシミュレーションを行うプログラム

#   ダイスを配列として定義
dice = [0 for i in range(6)]
#   ダイスの面を標準入力から取得
dice = list(input().split())
#   転がす方向を標準入力から取得
order = list(input())

for i in range(0, len(order)):
    #   S:5->1->2->6,5が1,1が2,,,
    if order[i] == "S":
        pass
    #   E:4->1->3->6
    elif order[i] == "E":
        pass
    #   W:3->1->4->6
    elif order[i] == "W":
        pass
    #   N:2->1->5->6
    elif order[i] == "N":
        pass