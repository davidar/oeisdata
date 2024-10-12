from math import isqrt
from sympy import primepi, mobius
def A000469(n):
    def f(x): return n+primepi(x)+x-sum(mobius(k)*(x//k**2) for k in range(1, isqrt(x)+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 02 2024
print([A000469(n) for n in range(1,31)])
