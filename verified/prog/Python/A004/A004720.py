def A004720(n):
    l = len(str(n-1))
    m = (10**l-1)//9
    k = n + l - 2 + int(n+l-1 >= m)
    return 0 if k == m else int(str(k).replace('1','')) # _Chai Wah Wu_, Apr 20 2021
print([A004720(n) for n in range(1,31)])
