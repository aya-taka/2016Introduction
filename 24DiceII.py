#   上面と前面の数字から、右側の面の数字を答えるプログラム

#   ダイスの面を定義するクラス
class Dice:
    def __init__(self):
        self.top = 1
        self.front = 2
        self.right = 3
        self.left = 4
        self.back = 5
        self.bottom = 6
    def turnSouth(self):
        temp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = temp
        return self
    def turnEast(self):
        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
        return self
    def turnWest(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp
        return self
    def turnNorth(self):
        temp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = temp
        return self

#   Diceの生成
myDice = Dice()
#   ダイス初期状態の入力
myDice.top, myDice.front, myDice.right, myDice.left, myDice.back, myDice.bottom = input().split()
#   質問の数qを標準入力から取得
q = int(input())
#   ループによる質問の読み込みと出力
#   出力対象 右側面 ダイステーブル換算(3)
for i in range(0, q):
    #   質問の読み込み 上面(1) 前面(2)　
    question = list(input())
    question = "".join(question).split()