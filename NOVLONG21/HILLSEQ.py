for test in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    main = []
    dup = []
    for i in t:
        if i in main:
            dup.append(i)
        else:
            main.append(i)
    if len(set(dup)) != len(dup):
        print(-1)
    else:
        print(dup + main[::-1])