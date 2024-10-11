def A003714(n):
    tlist, s = [1,2], 0
    while tlist[-1]+tlist[-2] <= n:
        tlist.append(tlist[-1]+tlist[-2])
    for d in tlist[::-1]:
        s *= 2
        if d <= n:
            s += 1
            n -= d
    return s # _Chai Wah Wu_, Jun 14 2018
print([A003714(n) for n in range(30)])
