for t in range(eval(input())):
    x, y, a, b, k = map(int, input().split())
    x += a * (k-1)
    y += b * (k-1)
    if x == y:
        print('SAME PRICE')
    elif x < y:
        print('PETROL')
    else:
        print('DIESEL')
