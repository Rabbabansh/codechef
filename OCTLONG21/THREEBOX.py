from math import ceil

for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    l = [a, b, c]
    s, n = 0, 1
    for i in l:
        s += i
        if s > d:
            n += 1
    print(n)
