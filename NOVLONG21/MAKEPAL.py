for t in range(eval(input())):
    n = eval(input())
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if i % 2 != 0:
            c += 1
    print(c // 2)
