from sympy import divisor_sigma
def a(n): return divisor_sigma(n, 3)
print([a(n) for n in range(1, 43)]) # _Michael S. Branicky_, Jan 09 2021