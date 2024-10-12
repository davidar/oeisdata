from sympy import integer_log
def A003595(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x): return n+x-sum(integer_log(x//7**i,5)[0]+1 for i in range(integer_log(x,7)[0]+1))
    return bisection(f,n,n) # _Chai Wah Wu_, Sep 16 2024
print([A003595(n) for n in range(1,31)])
