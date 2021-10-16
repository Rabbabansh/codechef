for t in range(int(input())):
    l = list(map(int, input().split()))

    ind, eng, draw = 0, 0, 0
    for i in l:
        if i == 0:
            draw += 1
        elif i == 1:
            ind += 1
        else:
            eng += 1

    if ind == eng:
        print("DRAW")
    elif max(eng, ind) == eng:
        print("ENGLAND")
    elif max(eng, ind) == ind:
        print("INDIA")
