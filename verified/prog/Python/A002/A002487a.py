from functools import lru_cache
@lru_cache(maxsize=None)
def a(n): return n if n<2 else a(n//2) if n%2==0 else a((n - 1)//2) + a((n + 1)//2) # _Indranil Ghosh_, Jun 08 2017; corrected by _Reza K Ghazi_, Dec 27 2021
print([a(n) for n in range(30)])
