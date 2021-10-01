from math import ceil, floor


def splitter(n):
    l = [ceil(n/2), floor(n/2)]
    return l


for t in range(int(input())):
    a, b = map(int, input().split())

    x, y = splitter(a), splitter(b)

    ans = (x[0] * y[0]) + (x[1] * y[1])
    print(ans)







