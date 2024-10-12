def A025502(n):
    m, tlist, s = 10**n, [1,2], 0
    while tlist[-1]+tlist[-2] <= m:
        tlist.append(tlist[-1]+tlist[-2])
    for d in tlist[::-1]:
        if d <= m:
            s += 1
            m -= d
    return s # _Chai Wah Wu_, Jun 14 2018
print([A025502(n) for n in range(30)])
