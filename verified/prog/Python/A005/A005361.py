from math import prod
from sympy import factorint
def a(n): return prod(factorint(n).values())
print([a(n) for n in range(1, 91)]) # _Michael S. Branicky_, Jul 04 2022