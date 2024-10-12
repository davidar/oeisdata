from functools import lru_cache
@lru_cache(maxsize=None)
def A002321(n):
    if n == 0:
        return 0
    c, j = n, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A002321(k1)
        j, k1 = j2, n//j2
    return j-c # _Chai Wah Wu_, Mar 30 2021
print([A002321(n) for n in range(1,31)])
