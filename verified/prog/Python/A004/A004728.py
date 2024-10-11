def A004728(n):
    l = len(str(n))
    m = 10**l-1
    k = n + l - int(n+l < m)
    return 8 if k == m else int(str(k).replace('9','')) # _Chai Wah Wu_, Apr 20 2021
print([A004728(n) for n in range(30)])
