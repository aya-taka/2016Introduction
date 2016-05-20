#   秒数を読み込んで、時間：分：秒に変換して出力するプログラム
second = int(input())
h = int(second / 3600)
m = int((second - (h * 3600)) / 60)
s = int(second % 60)
print("{0}:{1}:{2}".format(h, m, s))