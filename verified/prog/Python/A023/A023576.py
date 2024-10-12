from sympy import primefactors, prime
def a(n): return primefactors(prime(n) + 3)[-1]
print([a(n) for n in range(1, 72)]) # _Michael S. Branicky_, May 03 2021