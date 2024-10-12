from functools import lru_cache
@lru_cache(maxsize=None)
def A015650(n):
    if n == 0:
        return 0
    c, j = n+1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A015650(k1)
        j, k1 = j2, n//j2
    return n*(n+1)*(n+2)*(n+3)*(n+4)//120-c+j # _Chai Wah Wu_, Apr 18 2021
print([A015650(n) for n in range(1,31)])
