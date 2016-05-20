#   2つのサイコロが同一のものか判定するプログラム


#   ダイスの面を定義するクラス
#   top = 1 front = 2 right = 3 left = 4 back = 5 bottom = 6
class Dice:
    def __init__(self, nums):
        self.face = nums

    #   2->1->5->6
    def turnSouth(self):
        temp = self.face[0]
        self.face[0] = self.face[4]
        self.face[4] = self.face[5]
        self.face[5] = self.face[1]
        self.face[1] = temp
        return self

    #   4->1->3->6
    def turnEast(self):
        temp = self.face[0]
        self.face[0] = self.face[2]
        self.face[2] = self.face[5]
        self.face[5] = self.face[3]
        self.face[3] = temp
        return self

    #   3->1->4->6
    def turnWest(self):
        temp = self.face[0]
        self.face[0] = self.face[3]
        self.face[3] = self.face[5]
        self.face[5] = self.face[2]
        self.face[2] = temp
        return self

    #   5->1->2->6
    def turnNorth(self):
        temp = self.face[0]
        self.face[0] = self.face[1]
        self.face[1] = self.face[5]
        self.face[5] = self.face[4]
        self.face[4] = temp

    #   2->3->5->4
    def turnRight(self):
        temp = self.face[1]
        self.face[1] = self.face[2]
        self.face[2] = self.face[4]
        self.face[4] = self.face[3]
        self.face[3] = temp
        return self

    #   2->4->5->3
    def turnLeft(self):
        temp = self.face[1]
        self.face[1] = self.face[3]
        self.face[3] = self.face[4]
        self.face[4] = self.face[2]
        self.face[2] = temp
        return self

    def equals(self, another):
        #   上面の割り出し　前後方向
        for i in range(0, 4):
            if self.face[0] == another.face[0]:
                #   正面の割り出し　上面を変えずに回転
                for j in range(0, 4):
                    if self.face[1] == another.face[1]:
                        if self.face == another.face:
                            return True
                    another.turnRight()
            another.turnNorth()
        #   上面の割り出し　左右方向
        for i in range(0, 4):
            if self.face[0] == another.face[0]:
                #   正面の割り出し　上面を変えずに回転
                for j in range(0, 4):
                    if self.face[1] == another.face[1]:
                        if self.face == another.face:
                            return True
                    another.turnRight()
            another.turnEast()
        return False

#   Diceの生成
Dice1 = Dice(input().split())
Dice2 = Dice(input().split())

if Dice1.equals(Dice2):
    print("Yes")
else:
    print("No")
