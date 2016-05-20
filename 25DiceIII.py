#   2つのサイコロが同一のものか判定するプログラム

#   ダイスの面を定義するクラス
class Dice:
    def __init__(self):
        self.top = 1
        self.front = 2
        self.right = 3
        self.left = 4
        self.back = 5
        self.bottom = 6
    #   2->1->5->6
    def turnSouth(self):
        temp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = temp
        return self
    #   4->1->3->6
    def turnEast(self):
        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
        return self
    #   3->1->4->6
    def turnWest(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp
        return self

    #   5->1->2->6
    def turnNorth(self):
        temp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = temp
        return self
    #   2->3->5->4
    def turnRight(self):
        temp = self.front
        self.front = self.right
        self.right = self.back
        self.back = self.left
        self.left = temp
        return self
    #   2->4->5->3
    def turnRight(self):
        temp = self.front
        self.front = self.left
        self.left = self.back
        self.back = self.right
        self.right = temp
        return self
    def equals(self, Dice):
        if (self.top == Dice.top and self.front == Dice.front and self.bottom == Dice.bottom
            and self.back == Dice.back and self.right == Dice.right and self.left == Dice.left):
            return True
        else:
            return False

#   Diceの生成
Dice1 = Dice()
Dice2 = Dice()
#   ダイス初期状態の入力
Dice1.top, Dice1.front, Dice1.right, Dice1.left, Dice1.back, Dice1.bottom = input().split()
Dice2.top, Dice2.front, Dice2.right, Dice2.left, Dice2.back, Dice2.bottom = input().split()

#   ループによる質問の読み込みと出力
#   上面の割り出し　前後方向
for j in range(0, 3):
    if Dice1.top == Dice2.top:
        break
    Dice2.turnNorth()
#   上面の割り出し　左右方向
for j in range(0, 3):
    if Dice1.top == Dice2.top:
        break
    Dice2.turnEast()
#   正面の割り出し　上面を変えずに回転
for j in range(0, 3):
    if Dice1.front == Dice2.front:
        break
    Dice2.turnRight()
if Dice1.equals(Dice2):
    print("Yes")
else:
    print("No")
