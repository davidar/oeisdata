from sympy import mobius, integer_nthroot
def A007916(n):
    def f(x): return int(n+1-sum(mobius(k)*(integer_nthroot(x,k)[0]-1) for k in range(2,x.bit_length())))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 13 2024
print([A007916(n) for n in range(1,31)])
