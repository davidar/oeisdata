def A005260(n):
    m, g = 1, 0
    for k in range(n+1):
        g += m
        m = m*(n-k)**4//(k+1)**4
    return g # _Chai Wah Wu_, Oct 04 2022
print([A005260(n) for n in range(30)])
