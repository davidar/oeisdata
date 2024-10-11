from functools import lru_cache
from sympy import divisors
@lru_cache(maxsize=None)
def A002033(n):
    if n <= 1:
        return 1
    return sum(A002033(i-1) for i in divisors(n+1,generator=True) if i <= n) # _Chai Wah Wu_, Jan 12 2022
print([A002033(n) for n in range(30)])
