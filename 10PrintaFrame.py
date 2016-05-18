while 1:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(0, H):
        print("#", end="")
        for j in range(1, W - 1):
            if i == 0 or i == H - 1:
                print("#", end="")
            else:
                print(".", end="")

        print("#")
    print("")