def A004726(n):
    l = len(str(n))
    m = 7*(10**l-1)//9
    k = n + l - int(n+l < m)
    return 6 if k == m else int(str(k).replace('7','')) # _Chai Wah Wu_, Apr 20 2021
print([A004726(n) for n in range(30)])
