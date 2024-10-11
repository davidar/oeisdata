from sympy import divisor_sigma
def ok(n): return divisor_sigma(n, 2)%divisor_sigma(n, 1) == 0
print([k for k in range(1, 1300) if ok(k)]) # _Michael S. Branicky_, Feb 25 2024