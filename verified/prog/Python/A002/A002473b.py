from sympy import integer_log
def A002473(n):
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
        c = n+x
        for i in range(integer_log(x,7)[0]+1):
            i7 = 7**i
            m = x//i7
            for j in range(integer_log(m,5)[0]+1):
                j5 = 5**j
                r = m//j5
                for k in range(integer_log(r,3)[0]+1):
                    c -= (r//3**k).bit_length()
        return c
    return bisection(f,n,n) # _Chai Wah Wu_, Sep 16 2024
print([A002473(n) for n in range(1,31)])
