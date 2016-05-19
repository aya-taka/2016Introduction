#   上面と前面の数字から、右側の面の数字を答えるプログラム

#   ダイスを配列として定義
dice = [0 for i in range(6)]
#   ダイスの面を標準入力から取得
dice = list(input().split())
#   質問の数を標準入力から取得
question_number = int(input())

#   ループによる質問の読み込みと出力
for i in range(0, question_number):
    #   質問の読み込み
    question = list(input())
    question = "".join(question).split()
    print(question)