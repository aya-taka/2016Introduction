n = int(input())
a = input().split()
min = int(a[0])
max = int(a[0])
sum = 0
for i in a:
    if min > int(i):
        min = int(i)
    if max < int(i):
        max = int(i)
    sum += int(i)
print("{0} {1} {2}".format(min, max, sum))
