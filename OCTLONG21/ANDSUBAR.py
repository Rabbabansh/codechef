def displaysublist(A):
    B = [[]]

    for i in range(len(A) + 1):
        for j in range(i + 1, len(A) + 1):
            sub = A[i:j]
            B.append(sub)
    return B


def get_bitwiseAND(l):
    b = l[0]
    # print(len(l))
    for i in range(1, len(l)):
        if b == 0:
            return 0
            continue
        # print(b, l[i])
        b = b & l[i]
        # print(b)
    return b


for t in range(int(input())):  #
    # n = 5
    n = int(input())
    if n == 1:
        print(1)
        pass
    else:
        l = [x for x in range(1, n + 1)]
        # print(len(l))
        # if len(l) == 1:
        #     pass
        cringe = displaysublist(l)
        # print(cringe)

        based = []

        count = 1
        start = -n
        for i in range(n, 0, -1):
            start += i + 1
            count += i
            based.append(cringe[start:count])
        # print("this list is based")
        # print(based)
        based = based[1:]
        print(based)

        sol = 0

        for cringes in based:
            # cringes.reverse()
            # for c in cringes:
            #     lol = get_bitwiseAND(c)
            #     if lol == 0:
            #         pass
            #     elif len(c) > sol:
            #         sol = len(c)
            #         pass

            low = 0 
            high = len(cringes)
            mid = 0
            while low < high:
                mid = (high + low) // 2

                lol = get_bitwiseAND(cringes[mid])
                if lol == 0:
                    high = mid - 1
                elif lol != 0:
                    low = mid + 1
                    if len(cringes[mid]) > sol:
                        sol = len(cringes[mid])
        print(sol)
