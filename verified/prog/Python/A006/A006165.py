from functools import lru_cache
@lru_cache(maxsize=None)
def A006165(n): return 1 if n <= 2 else A006165(n//2) + A006165((n+1)//2) # _Chai Wah Wu_, Mar 08 2022
print([A006165(n) for n in range(1,31)])
