def A005261(n):
    m, g = 1, 0
    for k in range(n+1):
        g += m
        m = m*(n-k)**5//(k+1)**5
    return g # _Chai Wah Wu_, Oct 04 2022
print([A005261(n) for n in range(30)])
