from functools import lru_cache
@lru_cache(maxsize=None)
def A002083(n): return 1 if n <=3 else (A002083(n-1)<<1)-(A002083(n>>1) if n&1 else 0) # _Chai Wah Wu_, Nov 07 2022
print([A002083(n) for n in range(1,31)])
