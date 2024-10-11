def A005258(n):
    m, g = 1, 0
    for k in range(n+1):
        g += m
        m *= (n+k+1)*(n-k)**2
        m //= (k+1)**3
    return g # _Chai Wah Wu_, Oct 02 2022
print([A005258(n) for n in range(30)])
