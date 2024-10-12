from math import isqrt
from sympy import primepi, prime
def A001358(n):
    def f(x): return int(n+x-sum(primepi(x//prime(k))-k+1 for k in range(1, primepi(isqrt(x))+1)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Jul 23 2024
print([A001358(n) for n in range(1,31)])
