def A004724(n):
    l = len(str(n))
    m = 5*(10**l-1)//9
    k = n + l - int(n+l < m)
    return 4 if k == m else int(str(k).replace('5','')) # _Chai Wah Wu_, Apr 20 2021
print([A004724(n) for n in range(30)])
