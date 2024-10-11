from functools import lru_cache
from math import comb
@lru_cache(maxsize=None)
def A000364(n): return 1 if n == 0 else (1 if n % 2 else -1)*sum((-1 if i % 2 else 1)*A000364(i)*comb(2*n,2*i) for i in range(n)) # _Chai Wah Wu_, Jan 14 2022
print([A000364(n) for n in range(30)])
