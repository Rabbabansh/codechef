for t in range(int(input())):
    n = int(input())
    og_a = list(map(int, input().split()))
    ord_a = list(og_a)
    ord_a.sort(reverse=True)

    # print("og_a", og_a)
    # print("ord_a", ord_a)

    dict_a = {}
    for i in range(len(ord_a)):
        index_a = og_a.index(ord_a[i])
        dict_a[i] = index_a
        og_a[index_a] = -1
    # print("dict_a", dict_a)

    exh_c, ans_a = [], []
    rem_b = [-1] * (ord_a[0] + 1)
    # print("exh_c", exh_c)
    # print("rem_b", rem_b)

    for i in ord_a:
        ans = i - 1

        if i == 1:
            ans = 1
            rem_b[i] = 0
            ans_a.append(ans)
        elif ans not in exh_c:
            exh_c.append(ans)
            rem_b[i] = ans
            ans_a.append(ans + i)
        elif rem_b[i] != -1:
            if rem_b[i] == 0:
                ans = 0
                ans_a.append(i)
            else:
                rem_b[i] -= 1
                ans = rem_b[i]
                rem_b[i - 1] = ans
                rem_b[ans + 1] = ans
                exh_c.append(ans)
                ans_a.append(ans + i)

    og_ans = [0] * len(og_a)
    for i in range(len(og_ans)):
        og_ans[dict_a[i]] = ans_a[i]

    print(*og_ans)
