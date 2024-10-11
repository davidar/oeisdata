def A004727(n):
    l = len(str(n))
    m = 8*(10**l-1)//9
    k = n + l - int(n+l < m)
    return 7 if k == m else int(str(k).replace('8','')) # _Chai Wah Wu_, Apr 20 2021
print([A004727(n) for n in range(30)])
