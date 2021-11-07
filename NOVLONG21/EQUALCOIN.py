for t in range(eval(input())):
    x, y = map(int, input().split())
    xp = x * 1
    yp = y * 2

    tp = xp + yp
    hp = tp / 2

    if tp % 2 != 0:
        print("NO")
    elif tp == 0:
        print("NO")
    elif (x == 0) and (y % 2 != 0):
        print("NO")
    else:
        print("YES")
