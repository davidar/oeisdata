from math import isqrt, prod
from sympy import primerange, integer_nthroot, primepi
def A030059(n):
    def g(x,a,b,c,m): yield from (((d,) for d in enumerate(primerange(b+1,isqrt(x//c)+1),a+1)) if m==2 else (((a2,b2),)+d for a2,b2 in enumerate(primerange(b+1,integer_nthroot(x//c,m)[0]+1),a+1) for d in g(x,a2,b2,c*b2,m-1)))
    def f(x): return int(n+x-primepi(x)-sum(sum(primepi(x//prod(c[1] for c in a))-a[-1][0] for a in g(x,0,1,1,i)) for i in range(3,x.bit_length(),2)))
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
print([A030059(n) for n in range(1,31)])
