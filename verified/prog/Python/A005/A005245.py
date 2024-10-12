from functools import lru_cache
from itertools import takewhile
from sympy import divisors
@lru_cache(maxsize=None)
def A005245(n): return min(min(A005245(a)+A005245(n-a) for a in range(1,(n>>1)+1)),min((A005245(d)+A005245(n//d) for d in takewhile(lambda d:d*d<=n,divisors(n)) if d>1),default=n)) if n>1 else 1 # _Chai Wah Wu_, Apr 29 2023
print([A005245(n) for n in range(1,31)])
