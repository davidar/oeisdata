from functools import lru_cache
from sympy import divisors
@lru_cache(maxsize=None)
def divisor_tuple(n): # cached unordered tuple of divisors
    return tuple(divisors(n,generator=True))
@lru_cache(maxsize=None)
def A000081(n): return n if n <= 1 else sum(sum(d*A000081(d) for d in divisor_tuple(k))*A000081(n-k) for k in range(1,n))//(n-1) # _Chai Wah Wu_, Jan 14 2022
print([A000081(n) for n in range(30)])
