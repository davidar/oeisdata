from sympy import primepi
from sympy.ntheory.primetest import integer_nthroot
def A024619(n):
    def f(x): return int(n+1+sum(primepi(integer_nthroot(x,k)[0]) for k in range(1,x.bit_length())))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Jul 23 2024
print([A024619(n) for n in range(1,31)])
