from functools import lru_cache
from sympy import integer_nthroot, divisors
@lru_cache(maxsize=None)
def A003108(n):
    @lru_cache(maxsize=None)
    def a(n): return integer_nthroot(n,3)[1]
    @lru_cache(maxsize=None)
    def c(n): return sum(d for d in divisors(n,generator=True) if a(d))
    return (c(n)+sum(c(k)*A003108(n-k) for k in range(1,n)))//n if n else 1 # _Chai Wah Wu_, Jul 15 2024
print([A003108(n) for n in range(30)])
