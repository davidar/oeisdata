from functools import lru_cache
from math import comb
@lru_cache(maxsize=None)
def A000311(n): return n if n <= 1 else -(n-1)*A000311(n-1)+comb(n,m:=n+1>>1)*(0 if n&1 else A000311(m)**2) + (sum(comb(n,i)*A000311(i)*A000311(n-i) for i in range(1,m))<<1) # _Chai Wah Wu_, Nov 10 2022
print([A000311(n) for n in range(30)])
