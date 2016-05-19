#   上面と前面の数字から、右側の面の数字を答えるプログラム

#   ダイスを配列として定義
dice = [0 for i in range(6)]
#   ダイスの面を標準入力から取得
dice = list(input().split())
#   質問の数qを標準入力から取得
q = int(input())
#   ループによる質問の読み込みと出力
#   出力対象 右側面 ダイステーブル換算(3)
for i in range(0, q):
    #   質問の読み込み 上面(1) 前面(2)　
    question = list(input())
    question = "".join(question).split()
    #   東西方向に移動した形跡があるか
    if question[0] == dice[0] and question[1] == dice[1]:
        print("{0}".format(dice[2]))
    #   南北方向に移動した形跡があるか
    elif question[1] != dice[1]:
        pass
    print(question)