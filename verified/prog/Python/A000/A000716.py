from functools import lru_cache
from sympy import divisor_sigma
@lru_cache(maxsize=None)
def A000716(n): return sum(A000716(k)*divisor_sigma(n-k) for k in range(n))*3//n if n else 1 # _Chai Wah Wu_, Sep 25 2023
print([A000716(n) for n in range(30)])
