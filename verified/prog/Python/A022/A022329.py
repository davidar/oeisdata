from sympy import integer_log
def A022329(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return n+x-sum((x//3**i).bit_length() for i in range(integer_log(x,3)[0]+1))
    return integer_log((m:=bisection(f,n,n))>>(~m&m-1).bit_length(),3)[0] # _Chai Wah Wu_, Sep 15 2024
print([A022329(n) for n in range(1,31)])
