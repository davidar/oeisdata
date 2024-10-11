from sympy import prime
def a(n): return prime(prime(n))
print([a(n) for n in range(1, 52)]) # _Michael S. Branicky_, Aug 11 2021