def A004722(n):
    l = len(str(n))
    m = (10**l-1)//3
    k = n + l - int(n+l < m)
    return 2 if k == m else int(str(k).replace('3','')) # _Chai Wah Wu_, Apr 20 2021
print([A004722(n) for n in range(30)])
