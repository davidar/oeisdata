from math import gcd
from sympy import divisor_sigma
def ok(n): d = divisor_sigma(n, 1); return gcd(n, d) == 1
print([k for k in range(1, 134) if ok(k)]) # _Michael S. Branicky_, Mar 28 2022