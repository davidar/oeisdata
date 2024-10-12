from functools import lru_cache
@lru_cache(maxsize=None)
def A022825(n):
    if n <= 1:
        return n
    c, j = 0, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A022825(k1)
        j, k1 = j2, n//j2
    return c+n+1-j # _Chai Wah Wu_, Mar 31 2021
print([A022825(n) for n in range(1,31)])
