from functools import lru_cache
@lru_cache(maxsize=None)
def A001190(n):
    if n <= 1: return n
    m = n//2 + n % 2
    return sum(A001190(i+1)*A001190(n-1-i) for i in range(m-1)) + (1 - n % 2)*A001190(m)*(A001190(m)+1)//2 # _Chai Wah Wu_, Jan 14 2022
print([A001190(n) for n in range(30)])
