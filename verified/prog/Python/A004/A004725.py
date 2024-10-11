def A004725(n):
    l = len(str(n))
    m = 2*(10**l-1)//3
    k = n + l - int(n+l < m)
    return 5 if k == m else int(str(k).replace('6','')) # _Chai Wah Wu_, Apr 20 2021
print([A004725(n) for n in range(30)])
