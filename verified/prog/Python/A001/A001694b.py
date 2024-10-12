from math import isqrt
from sympy import mobius, integer_nthroot
def A001694(n):
    def squarefreepi(n):
        return int(sum(mobius(k)*(n//k**2) for k in range(1, isqrt(n)+1)))
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x):
        c, l = n+x, 0
        j = isqrt(x)
        while j>1:
            k2 = integer_nthroot(x//j**2,3)[0]+1
            w = squarefreepi(k2-1)
            c -= j*(w-l)
            l, j = w, isqrt(x//k2**3)
        c -= squarefreepi(integer_nthroot(x,3)[0])-l
        return c
    return bisection(f,n,n) # _Chai Wah Wu_, Sep 09 2024
print([A001694(n) for n in range(1,31)])
