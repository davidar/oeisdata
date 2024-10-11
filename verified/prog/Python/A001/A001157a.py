from sympy import divisor_sigma
def a(n): return divisor_sigma(n, 2)
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Jan 05 2021