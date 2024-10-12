from sympy import prime
from fractions import Fraction
def a(n): return sum(Fraction(1, prime(k)) for k in range(1, n+1)).numerator
print([a(n) for n in range(20)]) # _Michael S. Branicky_, Feb 12 2021