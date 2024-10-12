from sympy import primefactors, prime
def a(n): return sum(primefactors(prime(n) + 3))
print([a(n) for n in range(1, 70)]) # _Michael S. Branicky_, May 05 2021