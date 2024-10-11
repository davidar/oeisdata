from functools import lru_cache
from sympy import totient, proper_divisors
@lru_cache(maxsize=None)
def A007057(n): return (n<<n+1 if n&1 else 5*(n>>1)<<n)-sum(totient(n//d)*A007057(d) for d in proper_divisors(n,generator=True)) if n else 1 # _Chai Wah Wu_, Feb 19 2024
print([A007057(n) for n in range(30)])
