from math import prod
from sympy import factorint
def a(n): return prod((p**(e+1)-1)//(p-1) for p, e in factorint(n).items())
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Feb 25 2024