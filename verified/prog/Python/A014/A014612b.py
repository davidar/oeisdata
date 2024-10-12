from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A014612(n):
    def f(x): return int(n+x-sum(primepi(x//(k*m))-b for a,k in enumerate(primerange(integer_nthroot(x,3)[0]+1)) for b,m in enumerate(primerange(k,isqrt(x//k)+1),a)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 17 2024
print([A014612(n) for n in range(1,31)])
