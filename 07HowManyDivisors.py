a, b, c = map(int, input().split())
DivisorCount = 0
DivideNum = a
for var in range(a, b+1):
    if c % DivideNum == 0:
        DivisorCount += 1
    DivideNum += 1
print(DivisorCount)