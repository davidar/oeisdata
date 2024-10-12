from functools import lru_cache
@lru_cache(maxsize=None)
def A015613(n): # based on second formula in A018805
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(2*(A015613(k1)+k1)-1)
        j, k1 = j2, n//j2
    return (n*(n-3)-c+j)//2 # _Chai Wah Wu_, Mar 25 2021
print([A015613(n) for n in range(1,31)])
