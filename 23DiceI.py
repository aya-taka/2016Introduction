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
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    #   E:4->1->3->6
    elif order[i] == "E":
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
    #   W:3->1->4->6
    elif order[i] == "W":
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    #   N:2->1->5->6
    elif order[i] == "N":
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
print("{0}".format(dice[0]))