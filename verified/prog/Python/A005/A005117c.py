from math import isqrt
from sympy import mobius
def A005117(n):
    def f(x): return n+x-sum(mobius(k)*(x//k**2) for k in range(1, isqrt(x)+1))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Jul 22 2024
print([A005117(n) for n in range(1,31)])
