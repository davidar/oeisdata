from math import isqrt
from sympy import integer_nthroot
def A002760(n):
    def f(x): return n-1+x+integer_nthroot(x,6)[0]-integer_nthroot(x,3)[0]-isqrt(x)
    m, k = n-1, f(n-1)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 09 2024
print([A002760(n) for n in range(1,31)])
