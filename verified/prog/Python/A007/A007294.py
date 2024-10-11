from functools import lru_cache
from sympy import divisors
from sympy.ntheory.primetest import is_square
@lru_cache(maxsize=None)
def A007294(n):
    @lru_cache(maxsize=None)
    def a(n): return is_square((n<<3)+1)
    @lru_cache(maxsize=None)
    def c(n): return sum(d for d in divisors(n,generator=True) if a(d))
    return (c(n)+sum(c(k)*A007294(n-k) for k in range(1,n)))//n if n else 1 # _Chai Wah Wu_, Jul 15 2024
print([A007294(n) for n in range(30)])
