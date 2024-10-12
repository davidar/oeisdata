from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A014614(n):
    def f(x): return int(n+x-sum(primepi(x//(k*m*r*s))-d for a,k in enumerate(primerange(integer_nthroot(x,5)[0]+1)) for b,m in enumerate(primerange(k,integer_nthroot(x//k,4)[0]+1),a) for c,r in enumerate(primerange(m,integer_nthroot(x//(k*m),3)[0]+1),b) for d,s in enumerate(primerange(r,isqrt(x//(k*m*r))+1),c)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 17 2024
print([A014614(n) for n in range(1,31)])
