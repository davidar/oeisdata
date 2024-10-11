from functools import lru_cache
@lru_cache(maxsize=None)
def A018819(n): return 1 if n == 0 else A018819(n-1) + (0 if n % 2 else A018819(n//2)) # _Chai Wah Wu_, Jan 18 2022
print([A018819(n) for n in range(30)])
