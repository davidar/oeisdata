def A004721(n):
    l = len(str(n))
    m = 2*(10**l-1)//9
    k = n + l - int(n+l < m)
    return 1 if k == m else int(str(k).replace('2','')) # _Chai Wah Wu_, Apr 20 2021
print([A004721(n) for n in range(30)])
