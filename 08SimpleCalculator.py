while(1):
    a, op, b = map(input().split())
    if op == '?':
        break
    elif op == '+':
        print(int(a+b))