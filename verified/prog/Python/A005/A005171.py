from sympy import isprime
def a(n): return int(not isprime(n))
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Oct 28 2021