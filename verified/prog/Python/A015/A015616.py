from functools import lru_cache
@lru_cache(maxsize=None)
def A015616(n):
    if n <= 1:
        return 0
    c, j = n*(n-1)*(n-2)//6, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c -= (j2-j)*A015616(k1)
        j, k1 = j2, n//j2
    return c # _Chai Wah Wu_, Mar 30 2021
print([A015616(n) for n in range(1,31)])
