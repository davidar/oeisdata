def A005259(n):
    m, g = 1, 0
    for k in range(n+1):
        g += m
        m *= ((n+k+1)*(n-k))**2
        m //=(k+1)**4
    return g # _Chai Wah Wu_, Oct 02 2022
print([A005259(n) for n in range(30)])
