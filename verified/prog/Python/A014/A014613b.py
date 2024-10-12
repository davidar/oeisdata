from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A014613(n):
    def f(x): return int(n+x-sum(primepi(x//(k*m*r))-c for a,k in enumerate(primerange(integer_nthroot(x,4)[0]+1)) for b,m in enumerate(primerange(k,integer_nthroot(x//k,3)[0]+1),a) for c,r in enumerate(primerange(m,isqrt(x//(k*m))+1),b)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 17 2024
print([A014613(n) for n in range(1,31)])
