from functools import lru_cache
@lru_cache(maxsize=None)
def A002088(n): # based on second formula in A018805
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(2*A002088(k1)-1)
        j, k1 = j2, n//j2
    return (n*(n-1)-c+j)//2 # _Chai Wah Wu_, Mar 24 2021
print([A002088(n) for n in range(30)])
