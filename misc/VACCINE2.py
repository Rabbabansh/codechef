from math import ceil

for t in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    atRisk = 0

    i = n - 1
    while (a[i] >= 80 and i >= 0):
        atRisk += 1
        i -= 1

    j = 0
    while (a[j] <= 9 and j <= (n-1)):
        atRisk += 1
        j += 1

    notAtRisk = n - atRisk

    numOfDays = ceil(atRisk/d) + ceil(notAtRisk/d)
    print(numOfDays)
