def A004723(n):
    l = len(str(n))
    m = 4*(10**l-1)//9
    k = n + l - int(n+l < m)
    return 3 if k == m else int(str(k).replace('4','')) # _Chai Wah Wu_, Apr 20 2021
print([A004723(n) for n in range(30)])
