from functools import lru_cache
@lru_cache(maxsize=None)
def A015634(n):
    if n == 0:
        return 0
    c, j = 1, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*A015634(k1)
        j, k1 = j2, n//j2
    return n*(n+1)*(n+2)*(n+3)//24-c+j-n # _Chai Wah Wu_, Apr 18 2021
print([A015634(n) for n in range(1,31)])
