from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A007304(n):
    def f(x): return int(n+x-sum(primepi(x//(k*m))-b for a,k in enumerate(primerange(integer_nthroot(x,3)[0]+1),1) for b,m in enumerate(primerange(k+1,isqrt(x//k)+1),a+1)))
    kmin, kmax = 0,1
    while f(kmax) > kmax:
        kmax <<= 1
    while kmax-kmin > 1:
        kmid = kmax+kmin>>1
        if f(kmid) <= kmid:
            kmax = kmid
        else:
            kmin = kmid
    return kmax # _Chai Wah Wu_, Aug 29 2024
print([A007304(n) for n in range(1,31)])
