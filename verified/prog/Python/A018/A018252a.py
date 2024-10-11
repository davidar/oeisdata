from sympy import isprime
def ok(n): return not isprime(n)
print([k for k in range(1, 89) if ok(k)]) # _Michael S. Branicky_, Nov 10 2022