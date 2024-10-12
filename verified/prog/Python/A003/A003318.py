from functools import lru_cache
@lru_cache(maxsize=None)
def A003318(n):
    if n == 0:
        return 1
    c, j = n+1, 1
    k1 = (n-1)//j
    while k1 > 1:
        j2 = (n-1)//k1 + 1
        c += (j2-j)*A003318(k1)
        j, k1 = j2, (n-1)//j2
    return c-j # _Chai Wah Wu_, Mar 31 2021
print([A003318(n) for n in range(1,31)])
