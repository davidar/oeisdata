from functools import lru_cache
from sympy import totient, proper_divisors
@lru_cache(maxsize=None)
def A007055(n): return (n<<(n+1>>1) if n&1 else 3*n<<(n-2>>1))-sum(totient(n//d)*A007055(d) for d in proper_divisors(n,generator=True)) if n else 1 # _Chai Wah Wu_, Feb 18 2024
print([A007055(n) for n in range(30)])
