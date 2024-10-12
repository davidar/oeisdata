from math import isqrt
def A028982(n):
    def f(x): return n-1+x-isqrt(x)-isqrt(x>>1)
    kmin, kmax = 1,2
    while f(kmax) >= kmax:
        kmax <<= 1
    while True:
        kmid = kmax+kmin>>1
        if f(kmid) < kmid:
            kmax = kmid
        else:
            kmin = kmid
        if kmax-kmin <= 1:
            break
    return kmax # _Chai Wah Wu_, Aug 22 2024
print([A028982(n) for n in range(1,31)])
