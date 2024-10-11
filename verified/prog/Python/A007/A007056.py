from functools import lru_cache
from sympy import totient, proper_divisors
@lru_cache(maxsize=None)
def A007056(n): return (n*3**(1+(n>>1)) if n&1 else (n<<1)*3**(n>>1))-sum(totient(n//d)*A007056(d) for d in proper_divisors(n,generator=True)) if n else 1 # _Chai Wah Wu_, Feb 19 2024
print([A007056(n) for n in range(30)])
