while(1):
    a, op, b = input().split()
    if op == '?':
        break
    elif op == '+':
        print("{0}".format(int(a) + int(b)))
    elif op == '-':
        print("{0}".format(int(a) - int(b)))
    elif op == '*':
        print("{0}".format(int(a) * int(b)))
    elif op == '/':
        print("{0}".format(int(a) / int(b)))