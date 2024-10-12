from functools import lru_cache
from sympy import factorint
@lru_cache(maxsize=None)
def A023893(n):
    @lru_cache(maxsize=None)
    def c(n): return sum((p**(e+1)-p)//(p-1) for p,e in factorint(n).items())+1
    return (c(n)+sum(c(k)*A023893(n-k) for k in range(1,n)))//n if n else 1 # _Chai Wah Wu_, Jul 15 2024
print([A023893(n) for n in range(30)])
