from functools import lru_cache
@lru_cache(maxsize=None)
def A015631(n):
    if n == 0:
        return 0
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A015631(k1)
        j, k1 = j2, n//j2
    return n*(n-1)*(n+4)//6-c+j # _Chai Wah Wu_, Mar 30 2021
print([A015631(n) for n in range(1,31)])
