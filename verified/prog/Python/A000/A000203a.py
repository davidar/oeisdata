from sympy import divisor_sigma
def a(n): return divisor_sigma(n, 1)
print([a(n) for n in range(1, 71)]) # _Michael S. Branicky_, Jan 03 2021