from functools import lru_cache
@lru_cache(maxsize=None)
def A025523(n):
    if n == 0:
        return 1
    c, j = 2, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A025523(k1)
        j, k1 = j2, n//j2
    return n+c-j # _Chai Wah Wu_, Mar 30 2021
print([A025523(n) for n in range(1,31)])
