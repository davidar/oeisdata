from sympy import mobius, integer_nthroot
def A001597(n):
    def f(x): return int(n-2+x+sum(mobius(k)*(integer_nthroot(x,k)[0]-1) for k in range(2,x.bit_length())))
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
    return kmax # _Chai Wah Wu_, Aug 13 2024
print([A001597(n) for n in range(1,31)])
