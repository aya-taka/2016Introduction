#   辺の長さa,bを読み込んで、四角形の面積と全周を表示するプログラム
a, b = map(int, input().split())
print("{0} {1}".format(int(a * b), int(a + a + b + b)))