from functools import lru_cache
@lru_cache(maxsize=None)
def A018805(n): # based on second formula
    if n == 0:
        return 0
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A018805(k1)
        j, k1 = j2, n//j2
    return n*(n-1)-c+j # _Chai Wah Wu_, Mar 24 2021
print([A018805(n) for n in range(1,31)])
