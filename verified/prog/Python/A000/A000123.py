from functools import lru_cache
@lru_cache(maxsize=None)
def A000123(n): return 1 if n == 0 else A000123(n-1) + A000123(n//2) # _Chai Wah Wu_, Jan 18 2022
print([A000123(n) for n in range(30)])
