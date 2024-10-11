from math import comb
from functools import lru_cache
@lru_cache(maxsize=None)
def A000629(n): return 1+sum(comb(n,j)*A000629(j) for j in range(n)) if n else 1 # _Chai Wah Wu_, Sep 25 2023
print([A000629(n) for n in range(30)])
