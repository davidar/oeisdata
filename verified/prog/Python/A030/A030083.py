from sympy import isprime
def ok(n): return isprime(n) and set(str(n)) >= set(str(n**2))
print([k for k in range(10**6) if ok(k)]) # _Michael S. Branicky_, Nov 01 2023