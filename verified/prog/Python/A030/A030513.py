from math import isqrt
from sympy import primepi, integer_nthroot, primerange
def A030513(n):
    def f(x): return int(n+x-primepi(integer_nthroot(x,3)[0])+(t:=primepi(s:=isqrt(x)))+(t*(t-1)>>1)-sum(primepi(x//k) for k in primerange(1, s+1)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return m # _Chai Wah Wu_, Aug 16 2024
print([A030513(n) for n in range(1,31)])
