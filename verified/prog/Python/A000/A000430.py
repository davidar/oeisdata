from math import isqrt
from sympy import primepi
def A000430(n):
    def f(x): return n+x-primepi(x)-primepi(isqrt(x))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return int(m) # _Chai Wah Wu_, Aug 09 2024
print([A000430(n) for n in range(1,31)])
