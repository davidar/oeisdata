from math import prod
from sympy import factorint
def a(n): return prod((p-1)**e for p, e in factorint(n).items())
print([a(n) for n in range(1, 82)]) # _Michael S. Branicky_, Feb 27 2022