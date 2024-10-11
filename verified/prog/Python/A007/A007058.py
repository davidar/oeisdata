from functools import lru_cache
from sympy import totient, proper_divisors
@lru_cache(maxsize=None)
def A007058(n): return (n*5**(1+(n>>1)) if n&1 else 3*n*5**(n>>1))-sum(totient(n//d)*A007058(d) for d in proper_divisors(n,generator=True)) if n else 1 # _Chai Wah Wu_, Feb 19 2024
print([A007058(n) for n in range(30)])
