from sympy import primepi, integer_nthroot, primefactors
def A025473(n):
    if n == 1: return 1
    def f(x): return int(n+x-1-sum(primepi(integer_nthroot(x,k)[0]) for k in range(1,x.bit_length())))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return primefactors(m)[0] # _Chai Wah Wu_, Aug 15 2024
print([A025473(n) for n in range(1,31)])
