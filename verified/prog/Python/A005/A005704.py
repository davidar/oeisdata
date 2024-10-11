from functools import lru_cache
@lru_cache(maxsize=None)
def A005704(n): return A005704(n-1)+A005704(n//3) if n else 1 # _Chai Wah Wu_, Sep 21 2022
print([A005704(n) for n in range(30)])
