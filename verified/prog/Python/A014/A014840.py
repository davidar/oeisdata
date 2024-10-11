from math import gcd
from sympy.ntheory import digits
def a(n): return sum(sum(digits(n, b)[1:]) for b in range(2, n) if gcd(b, n) == 1)
print([a(n) for n in range(3, 62)]) # _Michael S. Branicky_, Sep 06 2022