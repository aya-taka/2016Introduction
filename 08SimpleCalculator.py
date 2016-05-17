while(1):
    a, op, b = input().split()
    if op == '?':
        break
    elif op == '+':
        print(int(a) + int(b))
    elif op == '-':
        print(int(a) - int(b))
    elif op == '*':
        print(int(a) * int(b))
    elif op == '/':
        print(int(int(a) / int(b)))