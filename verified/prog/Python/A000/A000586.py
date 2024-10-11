from sympy import isprime, primerange
from functools import cache
@cache
def a(n, k=None):
    if k == None: k = n
    if n < 1: return int(n == 0)
    return sum(a(n-p, p-1) for p in primerange(1, k+1))
print([a(n) for n in range(83)]) # _Michael S. Branicky_, Sep 03 2021 after _Charles R Greathouse IV_