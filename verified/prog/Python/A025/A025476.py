from sympy import primepi, integer_nthroot, primefactors
def A025476(n):
    def f(x): return int(n-1+x-sum(primepi(integer_nthroot(x,k)[0]) for k in range(2,x.bit_length())))
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
    return primefactors(kmax)[0] # _Chai Wah Wu_, Aug 15 2024
print([A025476(n) for n in range(1,31)])
