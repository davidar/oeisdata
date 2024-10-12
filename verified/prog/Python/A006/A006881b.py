from math import isqrt
from sympy import primepi, primerange
def A006881(n):
    def f(x): return int(n+x+(t:=primepi(s:=isqrt(x)))+(t*(t-1)>>1)-sum(primepi(x//k) for k in primerange(1, s+1)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 15 2024
print([A006881(n) for n in range(1,31)])
