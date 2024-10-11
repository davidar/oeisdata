from sympy import isprime
def ok(n): return n > 1 and not isprime(n)
print([k for k in range(89) if ok(k)]) # _Michael S. Branicky_, Nov 07 2021