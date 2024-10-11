from functools import lru_cache
from sympy import divisor_sigma
@lru_cache(maxsize=None)
def A000713(n): return sum(A000713(k)*((divisor_sigma(n-k)<<1)+1) for k in range(n))//n if n else 1 # _Chai Wah Wu_, Sep 25 2023
print([A000713(n) for n in range(30)])
